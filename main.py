from src import fetch_user_profile
from src import render_profile
from src import fetch_posts_from_bsky
from src import format_posts_list
from src import get_top_10_posts
from src import render_period_string
from src import top_hashtags
from src import format_hashtag_lists
from src import top_mentions
from tabulate import tabulate
import json
from pathlib import Path

if __name__ == "__main__":
    
    print("\n\n\n======================")
    print("\nWelcome to your Bluesky profile summary!\n")
    print("======================\n\n\n")

    print("Starting with fetching your app configuration!...\n")
    
    root_dir = Path.cwd()
    json_path = root_dir / "config.json"
    
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f) 

    print("Configuration loaded!\n\n\n")

    if data['get_profile']:
        if data['gen_avatar']:
            print(f"Fetching @{data['bsky_username']}'s profile and generating an avatar...\n")
        else:
            print(f"Fetching @{data['bsky_username']}'s profile without an avatar...\n")

        profile = fetch_user_profile(data['bsky_username'], gen_avatar=data['gen_avatar'])
        print("Profile loaded!\n\n\n")
        print(render_profile(profile))
        print("\n\n\n")

    if data['get_posts']:
        
        period_string = render_period_string(data['fetch_periond'])
        
        print(f"Fetching @{data['bsky_username']}'s posts for the period of {period_string}...\n")
        posts = fetch_posts_from_bsky(data['bsky_username'],data['fetch_periond'])
        print(f"Posts fetched!\n\n\n")
        
    if data['get_posts'] and data['get_top_posts']:
        print(f"Generating the list of top 10 posts...\n")
        top_10_posts = get_top_10_posts(posts)
        formatted_posts = format_posts_list(top_10_posts)
        print("\n\nYour top posts within last year:\n\n")
        print(tabulate(
            formatted_posts,
            headers=["Post Link", "Post Content", "Likes", "Interactions"],
            tablefmt="github",
            colalign=("left", "left", "right", "right"),
            ))  
        print("\n\n")

    if data['get_hashtags'] and data['get_posts']:
        print(f"Generating the list of top 10 hashtags...\n\n")
        top_used, top_by_interactions = top_hashtags(posts)
        
        if len(top_used) != 0:
            
            print(f"Top 10 hashtags used:\n")
            formatted_tags = format_hashtag_lists(top_used)
            print(tabulate(
                formatted_tags,
                headers=["Hashtag", "Posts tagged"],
                tablefmt="github",
                colalign=("left", "right"),
                ))  
            
            print("\n\nTop 10 hashtags by interactions:\n")

            formatted_tags = format_hashtag_lists(top_by_interactions)
            print(tabulate(
                formatted_tags,
                headers=["Hashtag", "Posts Interations"],
                tablefmt="github",
                colalign=("left", "right"),
                ))  

        else:
            print(f"No posts with hashtags found within this period.")

        print("\n\n")

    if data['get_mentions'] and data['get_posts']:
        print(f"Generating the list of top 10 mentions...\n\n")
        top_used, top_by_interactions, top_by_av = top_mentions(posts)
        
        if len(top_used) != 0:
            
            print(f"Top 10 mentioned users:\n")
            formatted_mentions = format_hashtag_lists(top_used)
            print(tabulate(
                formatted_mentions,
                headers=["User", "Posts tagged"],
                tablefmt="github",
                colalign=("left", "right"),
                ))  
            
            print("\n\nTop 10 mentions by interactions:\n")

            formatted_tags = format_hashtag_lists(top_by_interactions)
            print(tabulate(
                formatted_tags,
                headers=["User", "Posts Interations"],
                tablefmt="github",
                colalign=("left", "right"),
                ))
            
            print("\n\nTop 10 mentions by average interactions per post:\n")

            formatted_tags = format_hashtag_lists(top_by_av)
            print(tabulate(
                formatted_tags,
                headers=["User", "Average Post Interations"],
                tablefmt="github",
                colalign=("left", "right"),
                ))
            
            
        else:
            print(f"No posts with hashtags found within this period.")

        print("\n\n")
