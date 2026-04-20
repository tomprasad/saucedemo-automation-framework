from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest
@pytest.mark.e2e
def test_e2e_checkout_flow(logged_in_page):
    # Initialize page objects
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    # Verify on inventory page
    assert inventory_page.is_inventory_page_visible()

    # Add products to cart
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")

    # Verify items in cart badge
    assert inventory_page.get_cart_badge_count() == '2'

    # Navigate to cart
    inventory_page.open_cart()

    # Verify cart page
    assert cart_page.is_cart_page_visible()
    assert cart_page.get_cart_items_count() == 2

    # Proceed to checkout
    cart_page.click_checkout()

    # Complete checkout
    checkout_page.complete_checkout("John", "Doe", "12345")

    # Verify successful checkout
    success_message = checkout_page.get_success_message()
    assert "Thank you for your order!" in success_message