Feature: Writing a tweet

    Scenario: A user writes a tweet
        Given I am logged in as a user
        When I write a tweet
        Then the tweet should be stored