import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pages.accounts import Authenticate

@pytest.mark.accounts
class TestAccount:
    EMAIL = 'lbnewbegs2232@gmail.com'
    PASS = 'lbnewbegs2232'
        
    @pytest.mark.logins
    def test_login_success(self, browser):
        user = Authenticate(browser)
        user.login(self.EMAIL, self.PASS)
        user_name = browser.find_element_by_class_name('account').text
        
        assert user_name == 'Leight Booster'
        
    @pytest.mark.loginf
    def test_login_failed(self, browser):
        user = Authenticate(browser)
        user.login('abe34D@omail.com','Sdfe2eefg')
        failed_message = browser.find_element_by_css_selector('#center_column > div.alert.alert-danger > ol > li').text
        
        assert failed_message == 'Authentication failed.'
        
    
    @pytest.mark.logout
    def test_logout(self, browser):
        user = Authenticate(browser)
        user.login(self.EMAIL, self.PASS)
        user.logout()
        
        assert browser.find_element_by_class_name('login')
    
    @pytest.mark.resetpass
    def test_reset_password_success(self, browser):
        user = Authenticate(browser)
        user.reset_pass(self.EMAIL)
        success_message = browser.find_element_by_css_selector('#center_column > div > p.alert-success').text
        
        assert success_message == f'A confirmation email has been sent to your address: {self.EMAIL}'
    
    @pytest.mark.resetpassf
    def test_reset_password_failed(self, browser):
        user = Authenticate(browser)
        user.reset_pass('abe34D@omail.com')
        failed_message = browser.find_element_by_css_selector('#center_column > div > div.alert-danger li').text
        
        assert failed_message  == 'There is no account registered for this email address.'
        
        