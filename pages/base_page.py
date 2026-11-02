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

    def is_visible(self, locator, timeout: int = 60000) -> bool:
     logger.info(f"Checking visibility of element: {locator} (timeout={timeout} ms)")
     try:
         self.page.locator(locator).wait_for(state="visible", timeout=timeout)
         logger.info(f"Element is visible: {locator}")
         return True
     except Exception:
        logger.info(f"Element not visible within {timeout} ms: {locator}")
        return False