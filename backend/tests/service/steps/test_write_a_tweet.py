from pytest_bdd import scenarios, then, when

scenarios("../features/write_a_tweet.feature")


@when("I write a tweet", target_fixture="tweet")
def write_a_tweet(context, tweet_service):
    return tweet_service.create_tweet(
        author_id=context.user.user_id, tweet_text="My tweet text"
    )


@then("the tweet should be stored")
def check_tweet(tweet_service):
    all_tweets = tweet_service.tweet_repository.get_all()
    assert len(all_tweets) == 1
    assert all_tweets[0].text == "My tweet text"
