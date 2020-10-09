import pytest
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from gibberish import Gibberish
from pages.search import SearchBar
from pages.sorting import SortFilter

class TestSearch:
    
    gib = Gibberish()
    def test_random_clothes_result_count(self, browser):
        clothes = ['dress', 'blouse', 't-shirt']
        search_bar = SearchBar(browser)
        search_bar.search(random.choice(clothes))

        # Get only direct child elements from results using '*' in xpath
        results = browser.find_element_by_xpath("//ul[@class='product_list grid row']").find_elements_by_xpath('*')
        
        assert len(results)
    
    @pytest.mark.zero
    def test_zero_result(self, browser):
        search_bar = SearchBar(browser)
        search_bar.search(self.gib.generate_word())
        
        assert browser.find_element_by_css_selector('#center_column > p')
        
    @pytest.mark.sortprice
    def test_sort_price(self, browser):
        search_bar = SearchBar(browser)
        search_bar.search('dress')
        
        sort = SortFilter(browser)
        sort.by_price_asc()

        price_el = browser.find_elements_by_xpath("//div[@class='right-block']//span[@class='price product-price']")
        prices = [a.text for a in price_el]

        sorted_prices = sorted(prices)

        assert prices == sorted_prices
        
        
    @pytest.mark.sortname
    def test_sort_name(self, browser):
        search_bar = SearchBar(browser)
        search_bar.search('dress')
        
        sort = SortFilter(browser)
        sort.by_name_asc()

        name_el = browser.find_elements_by_css_selector("#center_column > ul  div > div.right-block > h5 > a")
        names = [a.text for a in name_el]

        sorted_names = sorted(names)

        assert names == sorted_names