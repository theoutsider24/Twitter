class Tweet:
    text: str
    author_id: str

    def __init__(self, text: str, author_id: str):
        self.text = text
        self.author_id = author_id

    @property
    def character_count(self):
        return len(self.text)


class User:
    id: str
    username: str

    def __init__(self, id: str, username: str):
        self.id = id
        self.username = username

    def is_author(self, tweet: Tweet):
        return self.id == tweet.author_id
