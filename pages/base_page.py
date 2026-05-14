from playwright.sync_api import Page

from utils.logger import get_logger


logger = get_logger()


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):

        logger.info(f"Clicking element: {locator}")

        self.page.locator(locator).click()

        logger.info(f"Successfully clicked element: {locator}")

    def fill(self, locator, text):

        logger.info(f"Entering text into element: {locator}")

        self.page.locator(locator).fill(text)

        logger.info(f"Successfully entered text into element: {locator}")

    def get_text(self, locator):

        logger.info(f"Fetching text from element: {locator}")

        text = self.page.locator(locator).text_content()

        logger.info(f"Fetched text: {text}")

        return text

    def is_visible(self, locator):

        logger.info(f"Checking visibility of element: {locator}")

        visible = self.page.locator(locator).is_visible()

        logger.info(f"Visibility status for {locator}: {visible}")

        return visible