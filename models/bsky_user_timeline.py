from models import UserProfile

class UserTimeline:

    def __init__ (self, user, posts={}):
        self.user = user
        self.posts = posts