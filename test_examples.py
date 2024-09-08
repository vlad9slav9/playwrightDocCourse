
def test_correct_login(login_page):
    inventory_page = login_page.login_with_standard_user()
    inventory_page.assert_shopping_cart_visible()


def test_incorrect_login(login_page):
    login_page.login_with_locked_out_user()
    login_page.assert_login_failed()


def test_add_cart(login_page):
    inventory_page = login_page.login_with_standard_user()
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()
    inventory_page.assert_item_in_cart()


def test_logout(login_page):
    inventory_page = login_page.login_with_standard_user()
    inventory_page.open_burger_menu()
    inventory_page.click_logout_button()
    inventory_page.assert_logged_out()


def test_switch_user(login_page):
    inventory_page = login_page.login_with_standard_user()
    inventory_page.add_item_to_cart()
    inventory_page.open_burger_menu()
    inventory_page.click_logout_button()

    inventory_page = login_page.login_with_problem_user()
    inventory_page.go_to_cart()
    inventory_page.assert_item_in_cart()