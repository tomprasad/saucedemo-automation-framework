from playwright.sync_api import sync_playwright
import pytest
from api.clients.user_client import UserClient
from pages.login_page import LoginPage

#Add command line options
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run Tests: chromium,firefox,webkit"
    )
#Playwright session setup
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright
#Browser Fixture
@pytest.fixture(scope="function")
def browser(playwright_instance,request):
    browser_name=request.config.getoption("--browser")
    if browser_name == 'chromium':
        browser=playwright_instance.chromium.launch(headless=True)
    elif browser_name == 'firefox':
        browser=playwright_instance.firefox.launch(headless=True)
    elif browser_name == 'webkit':
        browser=playwright_instance.webkit.launch(headless=True)
    else:
        raise ValueError('Invalid Browser Selected')
    yield browser
    browser.close()
#Page Fixture
@pytest.fixture(scope="function")
def page(browser):
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    context.close()
#API Fixture
@pytest.fixture(scope='session')
def user_client():
    return UserClient()
#Fixture that logs in a user and returns the logged-in page
@pytest.fixture(scope='function')
def logged_in_page(page):
    login_page=LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    return page


