from amazon.login_logout import login
from amazon.navigation import open_amazon_homepage


def test_login_logout(driver):
    open_amazon_homepage(driver)
    login(driver)
