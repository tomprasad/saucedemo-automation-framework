from playwright.sync_api import Page
from pages.base_page import BasePage
class CartPage(BasePage):
    CART_ITEM=".cart_item"
    CHECKOUT_BUTTON="[data-test='checkout']"
    REMOVE_BUTTON = "button[data-test^='remove']"
    CART_ITEM_NAME = ".inventory_item_name"
    def __init__(self,page:Page):
        super().__init__(page)
    #check if cart page is visible
    def is_cart_page_visible(self):
        return self.page.locator(self.CART_ITEM).first.is_visible()
    #Get number of items in cart
    def get_cart_items_count(self):
        return self.page.locator(self.CART_ITEM).count()
    #Get product names in cart
    def get_cart_product_names(self):
        items=self.page.locator(self.CART_ITEM_NAME).all_text_contents()
        return items
    #Remove item from cart
    def remove_product(self):
        self.page.locator(self.CART_ITEM).first.click()
    #Click checkout
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)