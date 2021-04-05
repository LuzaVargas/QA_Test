"""Scenario 1: User can search with “Google Search"""

import logging

from pages.result import GoogleResultPage
from pages.search import GoogleSearchPage

LOGGER = logging.getLogger(__name__)

def test_google_search(browser):
    
    search_page = GoogleSearchPage(browser)
    result_page = GoogleResultPage(browser)
    PHRASE = "test automation"
    WORD = "automation"

    # Given I’m on the homepage
    search_page.load()

    # When I type “test automation” into the search field And I click the Google Search button
    search_page.search(PHRASE)

    # Then I go to the search results page, and the first 3 results contain the word “automation”
    titles = result_page.result_titles()
    LOGGER.info("These are the results {}".format(titles))

    #Take the first 3 results
    for title in titles[0:3]:
        #LOGGER.info(title)
        assert WORD in title.lower()


def test_click_first_result(browser):
    
    search_page = GoogleSearchPage(browser)
    result_page = GoogleResultPage(browser)
    PHRASE = "test automation"
    WORD = "automation"

    # Given I Search by keyword
    search_page.load()
    search_page.search(PHRASE)

    # When I click on the first result link
    result_page.click_first_result()

    # Then I go to the page, and the page title contains the word “automation”
    LOGGER.info("Page title '{}'".format(result_page.title()))
    assert WORD in result_page.title().lower()