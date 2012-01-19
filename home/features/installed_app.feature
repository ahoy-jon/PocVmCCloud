Feature: Api to get informations about installed app

    Scenario: GET /api/installed-apps/
        Given I access the url "/api/installed-apps/"
        Then I see 2 apps at JSON format

    Scenario: DELETE /api/installed-apps/hello-world-01/
        Given I delete first app
        And I access the url "/api/installed-apps/"
        Then I see 1 apps at JSON format

    Scenario: POST /api/installed-apps/
        Given I send an app for installation
        And I access the url "/api/installed-apps/"
        Then I see 2 apps at JSON format

