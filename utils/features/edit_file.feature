Feature: Set installed app list from db inside nginx configuration file

    Scenario: Delete lines from a file
        Given I have a test file open with 5 lines
        When I delete line from 2 to 4
        Then The file contains 3 lines

    Scenario: Delete lines from nginx configuration file
        Given I open test nginx configuration file
        When I delete app list in configuration file
        Then I dont see app anymore in configuration file

    Scenario: Add lines to a file
        Given I have a test file open with 5 lines
        When I add two lines at given index
        Then The file contains 7 lines
        And my lines appears at given index

    Scenario: Add application to nginx configuration file
        Given I open test nginx configuration file
        And I delete app list in configuration file
        And I have two applications marked as installed in my DB
        When I set application list with installed application from DB
        Then Nginx configuration file has my two apps marked inside it


