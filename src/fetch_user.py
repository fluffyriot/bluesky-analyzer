import requests
import numpy as np
from PIL import Image,ImageFilter,ImageOps,ImageEnhance
from io import BytesIO
from models.bsky_user import UserProfile

def fetch_user_profile (user_name, gen_avatar):

    url = f"https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor={user_name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bluesky data: {e}\n")
        raise RuntimeError("Bluesky User details fetch failed.")

    if 'did' not in response:
        raise ValueError("Bluesky User not found!")

    fetched = UserProfile (
        did = response['did'].split(':')[-1],
        handle = response.get('handle', None),
        display_name = response.get('displayName', None),
        avatar_url = response.get('avatar', None),
        followers_count = response.get('followersCount', 0),
        follows_count = response.get('followsCount', 0),
        posts_count = response.get('postsCount', 0),
        joined_date = response.get('createdAt', None)
    )
    
    if (fetched.avatar_url != None and gen_avatar):
        fetched.avatar_string = get_terminal_avatar(response.get('avatar', None), width=32)

    return fetched

def get_terminal_avatar (image_url, width: int = 40, threshold: int = 75):
    
    BRAILLE_BASE = 0x2800
    DOT_MAP = [
    (0, 0), (1, 0), (2, 0), (0, 1),
    (1, 1), (2, 1), (3, 0), (3, 1)
    ]

    response = requests.get(image_url, timeout=10)
    response.raise_for_status()

    img = Image.open(BytesIO(response.content)).convert("L")
    img = ImageOps.autocontrast(img, cutoff=2)
    img = ImageEnhance.Contrast(img).enhance(2.0)
    img = img.filter(ImageFilter.GaussianBlur(radius=0.6))
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    aspect = img.height / img.width
    height = int(width * aspect * 0.5)

    img = img.resize((width * 2, height * 4), Image.LANCZOS)
    pixels = np.array(img)

    lines = []
    for y in range(0, pixels.shape[0], 4):
        row = []
        for x in range(0, pixels.shape[1], 2):
            bits = 0
            for i, (dy, dx) in enumerate(DOT_MAP):
                if pixels[y + dy, x + dx] < threshold:
                    bits |= 1 << i
            row.append(chr(BRAILLE_BASE + bits))
        lines.append("".join(row))

    return "\n".join(lines)
