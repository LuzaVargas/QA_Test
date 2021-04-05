"""
    This module contains GoogleResultPage,
    the page object for the Google Search Result Page.
"""
from selenium.webdriver.common.by import By

class GoogleResultPage:

    #Locators
    RESULT_LINKS = (By.ID, "res")
    SEARCH_INPUT = (By.XPATH, "//INPUT[@class='gLFyf gsfi']")
    RESULT_TITLES = (By.CSS_SELECTOR, "div.tF2Cxc div.yuRUbf h3")
    FIRST_LINK = (By.CSS_SELECTOR, "div.tF2Cxc div.yuRUbf a")

    #Initializer
    def __init__(self, browser):
        self.browser = browser
    
    #Interaction Methods
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def result_titles(self):
        results_h3 = self.browser.find_elements(*self.RESULT_TITLES)
        titles = []
        for result in results_h3:
            if result.text:
                titles.append(result.text)
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value
    
    def title(self):
        return self.browser.title

    def click_first_result(self):
        first_link = self.browser.find_element(*self.FIRST_LINK)
        first_link.click()