### Automation  Project

This automation project was done to give a solution to the following scenarios proposed for a test, using Pytest, Python and Selenium.

a) **Scenario 1:** User can search with "Google Search"
- Given I'm on the homepage
- When I type "test automation" into the search field And I click the Google Search button
- Then I go to the search results page, and the first 3 results contain the word "automation"

b) **Scenario 2:** User can go to the first search result
- Given I Search by keyword
- When I click on the first result link
- Then I go to the page, and the page title contains the word "automation"
