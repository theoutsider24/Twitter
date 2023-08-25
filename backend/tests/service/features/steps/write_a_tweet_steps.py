from behave import fixture, given, use_fixture, when, then, step
from mock import MagicMock
from twitter.domain.repository.tweet_repository import TweetRepositry
from twitter.domain.models import User

from twitter.service import TweetService
from unittest.mock import Mock


@fixture
def tweet_service(context):
    tweet_repository = TweetRepositry()
    context.tweet_service = TweetService(tweet_repository=tweet_repository)


@given("I am logged in as a user")
def set_user(context):
    context.user = User("my_user_id", "my_username")


@when("I write a tweet")
def write_a_tweet(context):
    use_fixture(tweet_service, context)
    context.tweet_text = "tweet_text"
    context.tweet = context.tweet_service.create_tweet(
        author=context.user, tweet_text="My tweet text"
    )


@then("the tweet should be stored")
def check_tweet(context):
    all_tweets = context.tweet_service.tweet_repository.get_all()
    assert len(all_tweets) == 1
    assert all_tweets[0].text == "My tweet text"
