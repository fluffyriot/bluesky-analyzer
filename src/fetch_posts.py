import requests
from models.bsky_post import SocialMediaPost
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
import re

def convert_period(period_string):
    pattern = (
        r"P"
        r"(?:(\d+)Y)?"
        r"(?:(\d+)M)?"
        r"(?:(\d+)D)?"
        r"(?:T"
        r"(?:(\d+)H)?"
        r"(?:(\d+)M)?"
        r"(?:(\d+)S)?"
        r")?"
    )

    match = re.fullmatch(pattern, period_string)
    if not match:
        raise ValueError(f"Invalid ISO-8601 duration: {period_string}")

    years, months, days, hours, minutes, seconds = (
        int(x) if x else 0 for x in match.groups()
    )

    return relativedelta(
        years=years,
        months=months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
    )

def post_in_period_check(created_dt, formatted_period):
    
    now = datetime.now(timezone.utc)
    threshold = now - formatted_period

    return created_dt >= threshold

def convert_embed_type(type_string):
    match type_string:
        case "app.bsky.embed.images":
            return "Image(s)"
        case "app.bsky.embed.video":
            return "Video"
        case "app.bsky.embed.external":
            return None
        case "app.bsky.embed.record":
            return "Quote"
        case "app.bsky.embed.recordWithMedia":
            return "Quote"
        case _:
            return type_string

def fetch_posts_from_bsky(bsky_username, period):
    
    url = f"https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor={bsky_username}&limit=100"

    response_set = []

    try:
        response = requests.get(url)
        response.raise_for_status()
        response_set += response.json()["feed"]
        
        while "cursor" in response.json():
            response = requests.get(url+"&cursor="+ response.json()["cursor"])
            response.raise_for_status()
            response_set += response.json()["feed"]
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bluesky data: {e}\nEmpty data will be returned.")
        return response_set
    
    return format_posts_to_class(response_array=response_set, original_username=bsky_username, period_string=period)
    
def format_posts_to_class(response_array, original_username, period_string):
    
    period = convert_period(period_string)

    formatted_set = []

    for item in response_array:
        
        created_formatted = datetime.fromisoformat(item["post"]["record"]["createdAt"].replace("Z", "+00:00"))

        if post_in_period_check(created_formatted, period):  
            
            if 'embed' in item["post"]["record"]:
                if '$type' in item["post"]["record"]['embed']:
                    embed_type = convert_embed_type(item["post"]["record"]['embed']['$type'])
            else:
                embed_type = None

            if "reply" in item["post"]["record"]:
                record_type = "Reply"
            elif item["post"]["author"]["handle"] != original_username:
                record_type = "Repost"
                if embed_type == "Quote":
                    embed_type = None
            elif embed_type == "Quote":
                embed_type = None
                record_type = "Quote"
            else: 
                record_type = "Post"
            
            formatted_post = SocialMediaPost(
                uri = item["post"]["uri"].split('/')[-1],
                author_handle = item["post"]["author"]["handle"],
                record_type = record_type,
                post_date = created_formatted,
                embed_type = embed_type,
                content = item["post"]["record"]["text"],
                bookmark_count = item["post"]["bookmarkCount"],
                reply_count = item["post"]["replyCount"],
                reposts_count = item["post"]["repostCount"],
                like_count = item["post"]["likeCount"],
                quote_count = item["post"]["quoteCount"]
                )
            
            formatted_post.update_interactions()
        
            formatted_set.append(formatted_post)

    return formatted_set