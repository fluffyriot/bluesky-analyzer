from models import SocialMediaPost

def get_top_10_posts (posts_array):
    
    convert_to_dict = [post.to_dict() for post in posts_array]

    top_10 = sorted(
        (post for post in convert_to_dict if post.get("record_type") == "Post"),
        key=lambda x: x["interactions_count"],
        reverse=True
        )[:10]
    
    revert_array = [SocialMediaPost(**post) for post in top_10]

    return revert_array