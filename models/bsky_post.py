class SocialMediaPost:

    def __init__(self, uri, author_did, record_type, post_date, embed_type, content, bookmark_count, reply_count, reposts_count, like_count):
        self.uri = uri
        self.author_did = author_did
        self.record_type = record_type
        self.post_date = post_date
        self.embed_type = embed_type
        self.content = content
        self.bookmark_count = bookmark_count
        self.reply_count = reply_count
        self.reposts_count = reposts_count
        self.like_count = like_count

