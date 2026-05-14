from playwright.sync_api import Page

from pages.base_page import BasePage
from utils.logger import get_logger


logger = get_logger()


class CartPage(BasePage):

    CART_ITEM = ".cart_item"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    REMOVE_BUTTON = "button[data-test^='remove']"
    CART_ITEM_NAME = ".inventory_item_name"

    def __init__(self, page: Page):
        super().__init__(page)

    # Check if cart page is visible
    def is_cart_page_visible(self):

        logger.info("Checking if cart page is visible")

        is_visible = self.page.locator(
            self.CART_ITEM
        ).first.is_visible()

        logger.info(f"Cart page visibility status: {is_visible}")

        return is_visible

    # Get number of items in cart
    def get_cart_items_count(self):

        logger.info("Fetching number of items in cart")

        count = self.page.locator(self.CART_ITEM).count()

        logger.info(f"Number of cart items: {count}")

        return count

    # Get product names in cart
    def get_cart_product_names(self):

        logger.info("Fetching product names from cart")

        items = self.page.locator(
            self.CART_ITEM_NAME
        ).all_text_contents()

        logger.info(f"Products in cart: {items}")

        return items

    # Remove item from cart
    def remove_product(self):

        logger.info("Removing product from cart")

        self.page.locator(self.REMOVE_BUTTON).first.click()

        logger.info("Product removed successfully")

    # Click checkout
    def click_checkout(self):

        logger.info("Proceeding to checkout")

        self.click(self.CHECKOUT_BUTTON)

        logger.info("Checkout button clicked successfully")