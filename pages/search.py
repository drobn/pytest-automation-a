from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchBar:
    
    SEARCH_INPUT = (By.ID, 'search_query_top')
    
    def __init__ (self, browser):
        self.browser = browser
    
    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)