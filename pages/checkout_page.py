from playwright.sync_api import Page
from pages.base_page import BasePage
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
        self.fill(self.FIRST_NAME_INPUT,first_name)
        self.fill(self.LAST_NAME_INPUT,last_name)
        self.fill(self.POSTAL_CODE_INPUT,postal_code)
    #Click continue Button
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
    #Click Finish Button
    def click_finish(self):
        self.click(self.FINISH_BUTTON)
    #Complete checkout flow
    def complete_checkout(self,first_name:str,last_name:str,postal_code:str):
        self.fill_checkout_information(first_name,last_name,postal_code)
        self.click_continue()
        self.click_finish()
    #Get success message
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)