from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
def test_product_added_to_cart(logged_in_page):
    inventory_page=InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    cart_page=CartPage(logged_in_page)
    cart_page.is_cart_page_visible()
    assert cart_page.get_cart_items_count() == 1