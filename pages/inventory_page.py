from playwright.async_api import Page

from pages.base_page import BasePage
from playwright.sync_api import expect

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.add_to_cart_button = self.page.locator("#add-to-cart-sauce-labs-backpack")
        self.shopping_cart_link = self.page.locator("[data-test=\"shopping-cart-link\"]")
        self.inventory_item_name = self.page.locator("[data-test=\"inventory-item-name\"]")
        self.burger_menu = self.page.locator("#react-burger-menu-btn")
        self.logout_sidebar_link = self.page.locator("[data-test=\"logout-sidebar-link\"]")
        self.login_button = self.page.locator("[data-test=\"login-button\"]")

    def add_item_to_cart(self):
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.shopping_cart_link.click()

    def assert_item_in_cart(self):
        expect(self.inventory_item_name).to_contain_text("Sauce Labs Backpack")

    def open_burger_menu(self):
        self.burger_menu.click()

    def click_logout_button(self):
        self.logout_sidebar_link.click()

    def assert_logged_out(self):
        expect(self.login_button).to_be_visible()
