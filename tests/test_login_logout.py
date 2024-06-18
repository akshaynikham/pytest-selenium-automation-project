from amazon.login_logout import login
from amazon.navigation import open_amazon_homepage
import allure


@allure.feature('login/logout')
@allure.story('testing valid/invalid scenarios')
def test_login_logout(driver):
    open_amazon_homepage(driver)
    login(driver)


