from datetime import timezone

class SocialMediaPost:

    def __init__(self, uri, author_handle, record_type, post_date, embed_type, content, bookmark_count, reply_count, reposts_count, like_count, quote_count):
        self.uri = uri
        self.author_handle = author_handle
        self.record_type = record_type
        self.post_date = post_date
        self.embed_type = embed_type
        self.content = content
        self.bookmark_count = bookmark_count
        self.reply_count = reply_count
        self.reposts_count = reposts_count
        self.like_count = like_count
        self.quote_count = quote_count
        self.interactions_count = 0

    def update_interactions(self):
        self.interactions_count = self.quote_count + self.like_count + self.reposts_count + self.reply_count + self.bookmark_count

    def to_dict(self) -> dict:
        return {
            "uri": self.uri,
            "author_handle": self.author_handle,
            "record_type": self.record_type,
            "post_date": self.post_date.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
            "embed_type": self.embed_type,
            "content": self.content,
            "bookmark_count": self.bookmark_count,
            "reply_count": self.reply_count,
            "reposts_count": self.reposts_count,
            "like_count": self.like_count,
            "quote_count": self.quote_count
        }

