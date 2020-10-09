import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = 'http://automationpractice.com'

@pytest.fixture()
def browser():
    driver = Chrome(ChromeDriverManager().install())

    driver.implicitly_wait(5)

    driver.maximize_window()
    
    driver.get(BASE_URL)

    driver.implicitly_wait(5)
    yield driver
    
    
    driver.quit()
    