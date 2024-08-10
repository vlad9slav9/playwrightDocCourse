from playwright.async_api import expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_correct_login(unauth_page: LoginPage):
    unauth_page.login("standard_user", "secret_sauce")
    unauth_page.assert_login_successful()


def test_incorrect_login(unauth_page: LoginPage):
    unauth_page.login("FalseName", "secret_sauce")
    unauth_page.assert_login_failed()


def test_add_cart(auth_page: InventoryPage):
    auth_page.add_item_to_cart()
    auth_page.go_to_cart()
    auth_page.assert_item_in_cart()


def test_logout(auth_page: InventoryPage):
    auth_page.open_burger_menu()
    auth_page.click_logout_button()
    auth_page.assert_logged_out()



