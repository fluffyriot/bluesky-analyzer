from models import SocialMediaPost
import re

def get_top_10_posts (posts_array):
    
    convert_to_dict = [post.to_dict() for post in posts_array]

    top_10 = sorted(
        (post for post in convert_to_dict if post.get("record_type") == "Post"),
        key=lambda x: x["interactions_count"],
        reverse=True
        )[:10]
    
    revert_array = [SocialMediaPost(**post) for post in top_10]

    return revert_array

def top_hashtags(posts):
    
    HASHTAG_PATTERN = re.compile(r"#\w+")

    hashtag_usage = {}
    hashtag_interactions = {}

    for post in posts:
        if not post.content:
            continue
        if post.record_type != "Post":
            continue

        hashtags = set(
            tag.lower()
            for tag in HASHTAG_PATTERN.findall(post.content)
        )

        for tag in hashtags:
            hashtag_usage[tag] = hashtag_usage.get(tag, 0) + 1
            hashtag_interactions[tag] = (
                hashtag_interactions.get(tag, 0) + post.interactions_count
            )

    top_used = dict(
        sorted(
            hashtag_usage.items(),
            key=lambda item: item[1],
            reverse=True
        )[:10]
    )

    top_by_interactions = dict(
        sorted(
            hashtag_interactions.items(),
            key=lambda item: item[1],
            reverse=True
        )[:10]
    )

    return top_used, top_by_interactions


def top_mentions(posts):
    HASHTAG_PATTERN = re.compile(r"@([\w\-]+(?:\.[\w\-]+)+)")

    mentions_count = {}
    mentions_interactions = {}

    for post in posts:
        if not post.content:
            continue
        if post.record_type != "Post":
            continue

        mentions_list = set(
            mention.lower()
            for mention in HASHTAG_PATTERN.findall(post.content)
        )

        for mention in mentions_list:
            key = "@" + mention
            mentions_count[key] = mentions_count.get(key, 0) + 1
            mentions_interactions[key] = mentions_interactions.get(key, 0) + post.interactions_count

    top_used = dict(
        sorted(
            mentions_count.items(),
            key=lambda item: item[1],
            reverse=True
        )[:10]
    )

    top_by_interactions = dict(
        sorted(
            mentions_interactions.items(),
            key=lambda item: item[1],
            reverse=True
        )[:10]
    )

    avg_interactions = {
        mention: mentions_interactions[mention] / mentions_count[mention]
        for mention in mentions_count
    }
    top_by_avg_interactions = dict(
        sorted(
            avg_interactions.items(),
            key=lambda item: item[1],
            reverse=True
        )[:10]
    )

    return top_used, top_by_interactions, top_by_avg_interactions

