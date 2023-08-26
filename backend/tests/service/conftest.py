from uuid import uuid4

from pytest import fixture
from pytest_bdd import given, parsers

from twitter.domain.models import Tweet, User
from twitter.domain.repository.tweet_repository import TweetRepositry
from twitter.service import TweetService


@fixture(name="context")
def context_fixture():
    # A class similar to Behave's context which allows a normal dict-type structure to be
    # accessed with dot notation
    class Context:
        def __init__(self):
            self._root = {}

            def __getattr__(self, attr):  # pylint: disable=unused-variable
                return self._root.get(attr)

            def __setattr__(self, attr, value):  # pylint: disable=unused-variable
                self._root[attr] = value

    return Context()


@fixture(name="tweet_service")
def tweet_service_fixture():
    tweet_repository = TweetRepositry()
    return TweetService(tweet_repository=tweet_repository)


@given("I am logged in as a user")
def set_user(context):
    context.user = User("my_user_id", "my_username")


@given(parsers.parse("{count:d} tweets have been written"))
def create_tweets(count, tweet_service):
    for _ in range(count):
        tweet_service.tweet_repository.add(
            Tweet(text="tweet_text", author_id=str(uuid4()))
        )
