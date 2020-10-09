import pytest
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.cart import Cart

@pytest.mark.cart
class TestCart:
    
    def test_cart_item_count(self, browser):
        cart = Cart(browser)
        
        cart.add_to_cart()
        cart.go_to_cart()
        
        items = len(cart.get_cart_items())
        
        assert items == 1