from pytest_bdd import parsers, scenarios, then, when

scenarios("../features/get_all_tweets.feature")


@when("I retrieve all tweets", target_fixture="tweets")
def get_all_tweets(tweet_service):
    return tweet_service.get_all_tweets()


@then(parsers.parse("I should see {count:d} tweets"))
def check_tweet(count, tweets):
    assert len(tweets) == count, tweets
