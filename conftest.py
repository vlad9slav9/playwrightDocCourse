import pytest

@pytest.fixture(scope="function")
def browser(playwright, browser_type):

    browser = playwright.chromium.launch(executable_path=r"C:\Program Files (x86)\krtech\chrome\chrome.exe", headless=False)

    yield browser

    browser.close()