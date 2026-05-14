from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.logger import get_logger
logger = get_logger()
class InventoryPage(BasePage):
    INVENTORY_LIST=".inventory_container"
    CART_ICON=".shopping_cart_link"
    CART_BADGE=".shopping_cart_badge"
    def __init__(self,page:Page):
        super().__init__(page)
    #Page Validation
    def is_inventory_page_visible(self):
            logger.info("Checking if Inventory Page is visible")
            return self.is_visible(self.INVENTORY_LIST)
    #Add product to cart
    def add_product_to_cart(self,product_name:str):
        logger.info(f"Adding product '{product_name}' to cart")
        add_button=self.page.locator(
                f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
            )
        add_button.click()
        logger.info(f"Product '{product_name}' added to cart")
    #Get Cart Badge count
    def get_cart_badge_count(self):
        logger.info("Getting cart badge count")
        if self.page.locator(self.CART_BADGE).is_visible():
            count = self.get_text(self.CART_BADGE)
            logger.info(f"Retrieved cart badge count: {count}")
            return count
        else:
            return '0'
    #Navigate to cart
    def open_cart(self):
        logger.info("Navigating to cart page")
        self.click(self.CART_BADGE)
        logger.info("Cart page opened")