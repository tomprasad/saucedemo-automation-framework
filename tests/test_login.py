from pages.login_page import LoginPage
from data.login_data import login_test_data
from playwright.sync_api import Page
import pytest
@pytest.mark.parametrize("username,password,expected_success",login_test_data)
def test_login(page:Page,username,password,expected_success):
    login_page=LoginPage(page)
    login_page.login(username,password)
    if expected_success:
        assert 'inventory' in page.url
    else:
        login_page.is_login_error_visible()

    
