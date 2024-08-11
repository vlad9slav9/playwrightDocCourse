import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_correct_login(unauth_page: LoginPage):
    unauth_page.login_with_standard_user()
    inventory_page = InventoryPage(unauth_page.page)
    inventory_page.assert_shopping_cart_visible()


def test_incorrect_login(unauth_page: LoginPage):
    unauth_page.login_with_locked_out_user()
    unauth_page.assert_login_failed()


@pytest.mark.parametrize("auth_page", ["standard_user"], indirect=True)
def test_add_cart(auth_page: InventoryPage):
    auth_page.add_item_to_cart()
    auth_page.go_to_cart()
    auth_page.assert_item_in_cart()


@pytest.mark.parametrize("auth_page", ["problem_user"], indirect=True)
def test_logout(auth_page: InventoryPage):
    auth_page.open_burger_menu()
    auth_page.click_logout_button()
    auth_page.assert_logged_out()


@pytest.mark.parametrize("auth_page", ["standard_user"], indirect=True)
def test_switch_user(auth_page: InventoryPage, unauth_page: LoginPage):
    auth_page.add_item_to_cart()
    auth_page.open_burger_menu()
    auth_page.click_logout_button()

    unauth_page.login_with_problem_user()

    inventory_page = InventoryPage(unauth_page.page)
    inventory_page.go_to_cart()
    inventory_page.assert_item_in_cart()



