from src import fetch_user_profile
from src import render_profile
from src import fetch_posts_from_bsky
import json

if __name__ == "__main__":
    # profile = fetch_user_profile(user_name="riot.photos", gen_avatar=False)
    # print(render_profile(profile))
    
    test = fetch_posts_from_bsky("riot.photos","P2Y1M0DT0H0M0S")

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump([post.to_dict() for post in test], f, ensure_ascii=False)

    print("test finished")
