from src import fetch_user_profile
from src import render_profile

if __name__ == "__main__":
    profile = fetch_user_profile("fluffyriot.com")
    print(render_profile(profile))
    