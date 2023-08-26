from twitter.domain.models import Tweet, User
from twitter.domain.repository.tweet_repository import TweetRepositry


class TweetService:
    def __init__(self, tweet_repository: TweetRepositry):
        self.tweet_repository = tweet_repository

    def create_tweet(self, author_id: str, tweet_text: str):
        tweet = Tweet(text=tweet_text, author_id=author_id)
        self.tweet_repository.add(tweet)
        return tweet
