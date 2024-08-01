import os
import pytest
import configparser

config = configparser.ConfigParser()
config.read('auth.ini')

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="gost", help="Choose browser: gost or yandex")

@pytest.fixture(scope="session")
def browser(playwright, request):
    browser_name = request.config.getoption("browser_name")
    #browser = None
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

    yield page

    context.close()

@pytest.fixture(scope="function")
def auth_page(browser):

    if os.path.exists("auth.json"):
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        page.goto("https://www.saucedemo.com/inventory.html")

    else:
        context = browser.new_context()
        page = context.new_page()

        username = config['credentials']['username']
        password = config['credentials']['password']

        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill(username)
        page.locator("#password").fill(password)
        page.locator("#login-button").click()

        context.storage_state(path="auth.json")

    yield page

    context.close()