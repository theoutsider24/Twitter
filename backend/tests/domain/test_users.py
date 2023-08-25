from pytest import fixture

from twitter.domain.models import User, Tweet


class TestUserIsAuthor:
    @fixture
    def user(self):
        return User(id="1", username="test")

    def test_user_is_author(self, user):
        tweet = Tweet(author_id=user.id, text="test")
        assert user.is_author(tweet)

    def test_user_is_not_author(self, user):
        tweet = Tweet(author_id="not_my_id", text="test")
        assert not user.is_author(tweet)
