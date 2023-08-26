Feature: Getting all tweets

    Scenario: A user retrieves all tweets
        Given I am logged in as a user
        And 10 tweets have been written
        When I retrieve all tweets
        Then I should see 10 tweets