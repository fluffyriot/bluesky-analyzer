from src import fetch_user_profile
from src import render_profile
from src import fetch_posts_from_bsky
from src import format_posts_list
from src import get_top_10_posts
from tabulate import tabulate
import json

if __name__ == "__main__":
    
    posts = fetch_posts_from_bsky("fluffyriot.com","P1Y0M0DT0H0M0S")
    posts = get_top_10_posts(posts)
    profile = fetch_user_profile(user_name="fluffyriot.com", gen_avatar=True)
    formatted_posts = format_posts_list(posts)
    print(render_profile(profile))

    print("\n\nYour top posts within last year:\n\n")
    
    print(tabulate(
        formatted_posts,
        headers=["Post Link", "Post Content", "Likes", "Interactions"],
        tablefmt="github",
        colalign=("left", "left", "right", "right"),
        ))  

    print("\n\n")
