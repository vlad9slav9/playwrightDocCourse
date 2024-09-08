import configparser

from playwright.async_api import Page
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = self.page.locator("#user-name")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")
        self.error_message = self.page.locator("[data-test=\"error\"]")

        self.config = configparser.ConfigParser()
        self.config.read('auth.ini')

    def navigate(self):
        self.page.goto("/")
        return self.page

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_login_failed(self):
        expect(self.error_message).to_contain_text("Epic sadface: Sorry, this user has been locked out.")

    def login_with_standard_user(self):
        username = self.config['standard_user']['username']
        password = self.config['standard_user']['password']
        self.login(username, password)
        return InventoryPage(self.page)

    def login_with_locked_out_user(self):
        username = self.config['locked_out_user']['username']
        password = self.config['locked_out_user']['password']
        self.login(username, password)

    def login_with_problem_user(self):
        username = self.config['problem_user']['username']
        password = self.config['problem_user']['password']
        self.login(username, password)
        return InventoryPage(self.page)
