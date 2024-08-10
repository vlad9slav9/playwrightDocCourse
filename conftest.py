import os
import pytest
import configparser
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

config = configparser.ConfigParser()
config.read('auth.ini')

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="gost", help="Choose browser: gost or yandex")

@pytest.fixture(scope="session")
def browser(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "gost":
        browser = playwright.chromium.launch(executable_path=r"C:\Program Files (x86)\krtech\chrome\chrome.exe", headless=False)
    elif browser_name == "yandex":
        browser = playwright.chromium.launch(executable_path=r"C:\Users\KSK-SHOP\AppData\Local\Yandex\YandexBrowser\Application\browser.exe", headless=False)
    else:
        raise pytest.UsageError("--browser_name should be gost or yandex")
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def unauth_page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com")
    yield LoginPage(page)
    context.close()

@pytest.fixture(scope="function")
def auth_page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")

    username = config['credentials']['username']
    password = config['credentials']['password']

    login_page = LoginPage(page)
    login_page.login(username, password)

    yield InventoryPage(page)
    context.close()
