from pages.base_page import BasePage
class LoginPage(BasePage):
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT= "[data-test='password']"
    LOGIN_BUTTON= "[data-test='login-button']"
    ERROR_MESSAGE="[data-test='error']"

    def login(self,username,password):
        self.fill(self.USERNAME_INPUT,username)
        self.fill(self.PASSWORD_INPUT,password)
        self.click(self.LOGIN_BUTTON)
    def get_error_msg(self):
        return self.get_text(self.ERROR_MESSAGE)
    def is_login_error_visible(self):
        return self.is_visible(self.ERROR_MESSAGE)
