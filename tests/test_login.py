from pages.login_page import LoginPage
from data.login_data import login_test_data
from playwright.sync_api import Page
import pytest
@pytest.mark.parametrize("username,password,success,expected_error",login_test_data)
def test_login(page:Page,username,password,success,expected_error):
    login_page=LoginPage(page)
    login_page.login(username,password)
    if success:
        assert 'inventory' in page.url
    else:
        error_message = login_page.get_error_msg()
        assert expected_error in error_message
        

    
