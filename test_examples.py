import re
from playwright.sync_api import Page, expect


def test_correct_login(unauth_page):

    unauth_page.locator("#user-name").fill("standard_user")
    unauth_page.locator("#password").fill("secret_sauce")
    unauth_page.locator("#login-button").click()

    expect(unauth_page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()

def test_incorrect_login(unauth_page):

    unauth_page.locator("#user-name").fill("FalseName")
    unauth_page.locator("#password").fill("secret_sauce")
    unauth_page.locator("#login-button").click()

    expect(unauth_page.locator("[data-test=\"error\"]")).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service")


def test_add_cart(auth_page):
    auth_page.locator("#add-to-cart-sauce-labs-backpack").click()
    auth_page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(auth_page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Backpack")


