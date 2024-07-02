import allure
from amazon.search import search_for_product
from amazon.navigation import open_amazon_homepage
from amazon.filters import apply_delivery_filter
from amazon.add_item_to_cart import add_items_to_cart
from amazon.utils import switch_window


@allure.feature("apply_product_filter")
@allure.description("apply product filter, select a product and add the product to cart")
@allure.testcase("apply single filter")
def test_apply_single_filter(driver):
    with allure.step("open home page"):
        open_amazon_homepage(driver)
    with allure.step("enter keyword mobile in the search box and submit"):
        search_for_product(driver, "mobile")
    with allure.step("apply_delivery_day"):
        apply_delivery_filter(driver, "Get It in 2 Days")
    with allure.step("switch to new window"):
        switch_window(driver)
    with allure.step("add item to cart"):
        add_items_to_cart(driver)

