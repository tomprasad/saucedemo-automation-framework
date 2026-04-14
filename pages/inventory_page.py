from playwright.sync_api import Page
from pages.base_page import BasePage
class InventoryPage(BasePage):
    INVENTORY_LIST=".inventory_container"
    CART_ICON=".shopping_cart_link"
    CART_BADGE=".shopping_cart_badge"
    def __init__(self,page:Page):
        super().__init__(page)
    #Page Validation
    def is_inventory_page_visible(self):
            return self.is_visible(self.INVENTORY_LIST)
    #Add product to cart
    def add_product_to_cart(self,product_name:str):
        add_button=self.page.locator(
                f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
            )
        add_button.click()
    #Get Cart Badge count
    def get_cart_badge_count(self):
        if self.page.locator(self.CART_BADGE).is_visible():
            return self.get_text(self.CART_BADGE)
        else:
            return '0'
    #Navigate to cart
    def open_cart(self):
        self.click(self.CART_BADGE)