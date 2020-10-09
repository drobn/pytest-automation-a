from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Authenticate:
    __LOG_IN_PG = (By.CLASS_NAME, 'login')
    __LOG_OUT_PG = (By.CLASS_NAME, 'logout')
    __RESET_PSS_PG = (By.LINK_TEXT, 'Forgot your password?')
    
    __EMAIL_FIELD = (By.ID, 'email')
    __PASS_FIELD = (By.ID, 'passwd')
    
    def __init__ (self, browser):
        self.browser = browser
    
    def login(self, email, password):
        self.browser.find_element(*self.__LOG_IN_PG).click()
        self.browser.find_element(*self.__EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*self.__PASS_FIELD).send_keys(password + Keys.RETURN)
    
    def logout(self):
        self.browser.find_element(*self.__LOG_OUT_PG).click()
    
    def reset_pass(self, email):
        self.browser.find_element(*self.__LOG_IN_PG).click()
        self.browser.find_element(*self.__RESET_PSS_PG).click()
        self.browser.find_element(*self.__EMAIL_FIELD).send_keys(email + Keys.RETURN)
        
    
        