from playwright.async_api import Page

from pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = self.page.locator("#user-name")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")
        self.error_message = self.page.locator("[data-test=\"error\"]")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_login_successful(self):
        expect(self.page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()

    def assert_login_failed(self):
        expect(self.error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")
