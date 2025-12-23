class UserProfile:

    def __init__(self,did,handle,display_name,avatar_url,followers_count,follows_count,posts_count,joined_date):
        self.did = did
        self.handle = handle
        self.display_name = display_name
        self.avatar_url = avatar_url
        self.followers_count = followers_count
        self.follows_count = follows_count
        self.posts_count = posts_count
        self.joined_date = joined_date
        self.avatar_string = ""

    def __repr__(self):
        return f"""Profile for @{self.handle}

User did: {self.did}
User name: {self.display_name}
User joined date: {self.joined_date}
User posted: {self.posts_count}
User followers / follows: {self.followers_count} / {self.follows_count}

This is them (well... kinda... :D ):
{self.avatar_string}

"""