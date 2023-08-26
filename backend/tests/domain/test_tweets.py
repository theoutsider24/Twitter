from twitter.domain.models import Tweet


class TestTweetCharacterLength:
    def test_tweet_character_length(self):
        tweet = Tweet(text="test", author_id="1")
        assert tweet.character_count == 4
