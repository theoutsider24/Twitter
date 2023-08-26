from typing import List

from twitter.domain.models import Tweet
from twitter.domain.repository.tweet_repository import TweetRepositry


class TweetService:
    tweet_repository: TweetRepositry

    def __init__(self, tweet_repository: TweetRepositry):
        self.tweet_repository = tweet_repository

    def create_tweet(self, author_id: str, tweet_text: str) -> Tweet:
        tweet = Tweet(text=tweet_text, author_id=author_id)
        self.tweet_repository.add(tweet)
        return tweet

    def get_all_tweets(self) -> List[Tweet]:
        return self.tweet_repository.get_all()
