
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


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
    login_page = LoginPage(page)
    login_page.navigate()
    yield login_page
    context.close()


@pytest.fixture(scope="function")
def auth_page(request, unauth_page: LoginPage):
    user_type = request.param

    if user_type == "standard_user":
        unauth_page.login_with_standard_user()
    elif user_type == "problem_user":
        unauth_page.login_with_problem_user()
    elif user_type == "locked_out_user":
        unauth_page.login_with_locked_out_user()
    else:
        raise ValueError(f"Unsupported user type: {user_type}")

    inventory_page = InventoryPage(unauth_page.page)

    yield inventory_page
