from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class SortFilter:
    
    __SORT_BAR = (By.ID, 'selectProductSort')
    
    __PRICE_ASC = 'price:asc'
    __PRICE_DSC = 'price:desc'
    __NAME_ASC = 'name:asc'
    __NAME_DSC = 'name:desc'
    __QTY_DSC = 'quantity:desc'
    __REF_ASC = 'reference:asc'
    __REF_DSC = 'reference:desc'
    
    def __init__ (self, browser):
        self.browser = browser
    
    def by_price_asc(self):
        sort = Select(self.browser.find_element(*self.__SORT_BAR))
        sort.select_by_value(self.__PRICE_ASC)
    
    def by_price_dsc(self):
        sort = Select(self.browser.find_element(*self.__SORT_BAR))
        sort.select_by_value(self.__PRICE_DSC)
    
    def by_name_asc(self):
        sort = Select(self.browser.find_element(*self.__SORT_BAR))
        sort.select_by_value(self.__NAME_ASC)   
    
    def by_name_dsc(self):
        sort = Select(self.browser.find_element(*self.__SORT_BAR))
        sort.select_by_value(self.__NAME_DSC)
    
    def by_qty_dsc(self):
        sort = Select(self.browser.find_element(*self.__SORT_BAR))
        sort.select_by_value(self.__QTY_DSC)
    
    def by_ref_asc(self):
        sort = Select(self.browser.find_element(*self.__SORT_BAR))
        sort.select_by_value(self.__REF_ASC)
    
    def by_ref_dsc(self):
        sort = Select(self.browser.find_element(*self.__SORT_BAR))
        sort.select_by_value(self.__REF_DSC)
    