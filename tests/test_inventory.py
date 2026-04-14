from pages.inventory_page import InventoryPage
def test_add_product_to_cart(logged_in_page):
    inventory_page=InventoryPage(logged_in_page)
    inventory_page.is_inventory_page_visible()
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    assert inventory_page.get_cart_badge_count() == '1'

