from datetime import datetime
from models import UserProfile
from models import SocialMediaPost
import re

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"  # supplemental symbols & pictographs
    "\U0001FA00-\U0001FAFF"
    "\U00002702-\U000027B0"  # dingbats
    "\U000024C2-\U0001F251"
    "\u200D"
    "]+",
    flags=re.UNICODE
)

def strip_emojis(text):
    return EMOJI_PATTERN.sub(" [] ", text)

def format_posts_list(posts):
    return_table = []

    for post in posts:
        post_url = post.get_url()
        content_upd = f"{strip_emojis(post.content.replace("\n"," "))[:47]}..."
        return_table.append((post_url, content_upd, post.like_count, post.interactions_count))

    return return_table

def render_profile(profile = UserProfile, width = 76):
    
    if profile.avatar_string != None:
        lines = profile.avatar_string.split('\n')
    else:
        lines = []

    inner = width - 4
    fields = [
        ("Handle", profile.handle),
        ("Display Name", strip_emojis(profile.display_name)),
        ("User DID", profile.did),
        ("Joined", profile.joined_date),
        ("Posts", f"{profile.posts_count:,}"),
        ("Followers", f"{profile.followers_count:,}"),
        ("Following", f"{profile.follows_count:,}"),
    ]

    label_width = max(len(label) for label, _ in fields)

    title = f" {profile.handle} "
    lines.append("┌" + title.center(width - 2, "─") + "┐")

    for label, value in fields:
        row = f"{label.ljust(label_width)} : {value}"
        lines.append(f"│ {row.ljust(inner)} │")

    lines.append("└" + "─" * (width - 2) + "┘")
    return "\n".join(lines)