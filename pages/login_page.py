from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class LoginPage(BasePage):
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT= "[data-test='password']"
    LOGIN_BUTTON= "[data-test='login-button']"
    ERROR_MESSAGE="[data-test='error']"

    def login(self,username,password):
        logger.info(f"Attempting to log in with username: {username}")
        self.fill(self.USERNAME_INPUT,username)
        self.fill(self.PASSWORD_INPUT,password)
        self.click(self.LOGIN_BUTTON)
        logger.info("Login button clicked")
    def get_error_msg(self):
        logger.info(f"Retrieving error message")
        return self.get_text(self.ERROR_MESSAGE)
    
