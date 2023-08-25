class Tweet:
    text: str
    author_id: str

    def __init__(self, text: str, author_id: str):
        self.text = text
        self.author_id = author_id


class User:
    id: str
    username: str

    def __init__(self, id: str, username: str):
        self.id = id
        self.username = username
