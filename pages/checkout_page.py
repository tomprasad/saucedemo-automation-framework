from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.logger import get_logger
logger = get_logger()
class CheckoutPage(BasePage):
    FIRST_NAME_INPUT="[data-test='firstName']"
    LAST_NAME_INPUT="[data-test='lastName']"
    POSTAL_CODE_INPUT="[data-test='postalCode']"
    CONTINUE_BUTTON="[data-test='continue']"
    FINISH_BUTTON="[data-test='finish']"
    SUCCESS_MESSAGE=".complete-header"
    def __init__(self,page:Page):
        super().__init__(page)
    #Fill checkout information
    def fill_checkout_information(self,first_name:str,last_name:str,postal_code:str):
        logger.info(f"Filling checkout information for {first_name} {last_name} {postal_code}")
        self.fill(self.FIRST_NAME_INPUT,first_name)
        self.fill(self.LAST_NAME_INPUT,last_name)
        self.fill(self.POSTAL_CODE_INPUT,postal_code)
        logger.info("Checkout information filled successfully")
    #Click continue Button
    def click_continue(self):
        logger.info("Clicking continue button")
        self.click(self.CONTINUE_BUTTON)
        logger.info("Continue button clicked successfully")
    #Click Finish Button
    def click_finish(self):
        logger.info("Clicking finish button")
        self.click(self.FINISH_BUTTON)
        logger.info("Finish button clicked successfully")
    #Complete checkout flow
    def complete_checkout(self,first_name:str,last_name:str,postal_code:str):
        self.fill_checkout_information(first_name,last_name,postal_code)
        self.click_continue()
        self.click_finish()
        logger.info("Checkout flow completed successfully")
    #Get success message
    def get_success_message(self):
        logger.info("Retrieving success message")
        return self.get_text(self.SUCCESS_MESSAGE)