Feature: Api to get informations about installed app

    Scenario: GET /api/installed-apps/
        Given I access the url "/api/installed-apps/"
        Then I see two apps at JSON format
