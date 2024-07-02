from amazon.login_logout import login, logout
from amazon.navigation import open_amazon_homepage
import allure


@allure.feature('login_logout')
@allure.description('validating login and logout feature')
@allure.testcase("valid login and logout")
def test_login_logout(driver):
    with allure.step("open_amazon_homepage"):
        open_amazon_homepage(driver)
    with allure.step("login"):
        login(driver)
    with allure.step("logout"):
        logout(driver)
