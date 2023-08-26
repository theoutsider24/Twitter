from typing import List

from twitter.domain.models import Tweet


class TweetRepositry:
    def __init__(self):
        self.tweets = []

    def add(self, tweet: Tweet):
        self.tweets.append(tweet)

    def get_all(self) -> List[Tweet]:
        return self.tweets
