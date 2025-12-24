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
3. Create a new **config.json** in the following format you can copy:
```
{
    "bsky_username": "fluffyriot.com", // your Bluesky handle
    "fetch_periond": "P0Y3M0DT0H0M0S", // fetch period for posts
    "get_posts": true, // check if you want to get posts for analysis
    "get_top_posts": true, // check if you want to print a list of top 10 posts (only works with get_posts set to true)
    "gen_avatar": true, // check if you want to print terminal representation of your avatar
    "get_profile": true, // check if you want to print details of your profile
    "get_hashtags": true, // check if you want to print a list of top hashtags (only works with get_posts set to true)
    "get_mentions": true // check if you want to print a list of top mentions (only works with get_posts set to true)
}
```
4. In your terminal switch to the downloaded folder
5. Run ```venv venv -m```
6. Run ```make```
7. Run ```python3 main.py```
