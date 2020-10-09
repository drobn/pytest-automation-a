import pytest
import requests
from time import sleep

class TestHomepage:
    def test_title(self, browser):
        assert 'My Store' == browser.title
    
    def test_search_box(self, browser):
        assert browser.find_element_by_id('search_query_top')
        
    def test_image_carousel(self, browser):
        image_nav = browser.find_element_by_class_name('bx-prev')

        for _ in range(3): 
            sleep(5)
            image_nav.click()
            
        assert image_nav
    
    @pytest.mark.linktest
    def test_all_links(self, browser):
        status_codes = []
        temp = [l.get_attribute('href') for l in browser.find_elements_by_tag_name('a')]
        links = [i for i in temp if 'http' in i]
        
        print('Total links: ',len(links))
        # pytest.set_trace()
        for a in links:
            if '200' in str(requests.head(a)):
                status_codes = str(requests.head(a))     
            else:
                status_codes = 'error'

        assert 'error' not in status_codes
        

        
        

        