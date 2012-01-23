Feature: Api to get informations about installed app

    Scenario: GET /api/market/apps/
        Given I access the url "/api/market/apps/"
        Then I see 2 apps at JSON format


