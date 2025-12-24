# Welcome to Bluesky Analyzer!

This is my first independent project for my boot.dev course.

I'm going to continue developing it, but at this moment it can:
- Get your general profile information
- Generate console image from your avatar
- Pull out your top posts
- Your top hashtags
- Your top mentions

## Getting started

1. Ensure ```[make](https://www.gnu.org/software/make/)``` is installed.
2. Download the whole project
3. Create a new **config.json** in the following format you can copy below:
```
{
    "bsky_username": "fluffyriot.com",
    "fetch_periond": "P0Y3M0DT0H0M0S",
    "get_posts": true,
    "get_top_posts": true,
    "gen_avatar": true,
    "get_profile": true,
    "get_hashtags": true,
    "get_mentions": true
}
```
4. In your terminal switch to the downloaded folder
5. Run ```venv venv -m```
6. Run ```make```
7. Run ```python3 main.py```
