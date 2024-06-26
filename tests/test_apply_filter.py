import allure
from amazon.search import search_for_product
from amazon.navigation import open_amazon_homepage
from amazon.filters import apply_brand_filter, apply_delivery_filter


# @allure.testcase()
def test_apply_single_filter(driver):
    with allure.step("open home page"):
        open_amazon_homepage(driver)
    with allure.step("enter keyword mobile in the search box and submit"):
        search_for_product(driver, "mobile")
    # with allure.step("apply_brand_filter"):
    #     apply_brand_filter(driver, "Redmi")
    with allure.step("apply_delivery_day"):
        apply_delivery_filter(driver, "Get It in 2 Days")
