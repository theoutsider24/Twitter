from datetime import datetime


class Tweet:
    text: str
    author_id: str
    created_date: datetime

    def __init__(
        self,
        text: str,
        author_id: str,
    ):
        self.text = text
        self.author_id = author_id
        self.created_date = datetime.now()

    @classmethod
    def create(cls, author_id, text) -> "Tweet":
        if len(text) > 280:
            raise ValueError("Tweet is too long")
        return cls(text, author_id)

    @property
    def character_count(self):
        return len(self.text)

    def as_dict(self):
        return {
            "text": self.text,
            "author_id": self.author_id,
            "created_date": self.created_date.isoformat(),
        }


class User:
    user_id: str
    username: str

    def __init__(self, user_id: str, username: str):
        self.user_id = user_id
        self.username = username

    def is_author(self, tweet: Tweet):
        return self.user_id == tweet.author_id
