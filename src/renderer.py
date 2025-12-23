from datetime import datetime
from models.bsky_user import UserProfile

def render_profile(profile = UserProfile, width = 76):
    
    lines = profile.avatar_string.split('\n')

    inner = width - 4
    fields = [
        ("Handle", profile.handle),
        ("Display Name", profile.display_name),
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