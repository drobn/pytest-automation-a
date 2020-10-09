from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Cart:
    
    # __ITEMS = (By.XPATH, '//*[@id="cart_summary"]/tbody/*')
    __ITEMS = (By.CSS_SELECTOR, '#cart_summary > tbody > *')
    CART = (By.CSS_SELECTOR, '#header > div:nth-child(3) > div > div > div:nth-child(3) > div > a')
    
    ITEM_1 = (By.XPATH, '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]/span')

    # UNIT_PRICE = (By.ID, '')
    # QTY = ()
    # UNIT_TOTAL =() 
    # PRODUCT_TOTALS = () 
    # SHIPPING = ()
    # TAX = ()
    # TOTALS = () 
    
    def __init__ (self, browser):
        self.browser = browser
    
    def go_to_cart(self):
        self.browser.find_element(*self.CART).click()
    
    def get_cart_items(self):
        return self.browser.find_elements(*self.__ITEMS)
    
    def add_to_cart(self):
        el = self.browser.find_element_by_css_selector('#homefeatured > :nth-child(1)')
        hov = ActionChains(self.browser).move_to_element(el)
        hov.perform()
        
        self.browser.find_element(*self.ITEM_1).click()
        self._close_popup_window()
        
        
    def _close_popup_window(self):
        self.browser.find_element_by_xpath('//*[@title="Close window"]').click()