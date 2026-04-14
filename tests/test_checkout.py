from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
def test_complete_checkout(logged_in_page):
    inventory_page=InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    cart_page=CartPage(logged_in_page)
    cart_page.click_checkout()
    checkout_page=CheckoutPage(logged_in_page)
    checkout_page.complete_checkout("Tom", "QA", "12345")
    assert 'Thank you for your order' in checkout_page.get_success_message()




