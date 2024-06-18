from amazon.search import search_for_product, get_search_results_title, get_product_titles, select_product, switch_window
from amazon.navigation import open_amazon_homepage
from amazon.add_item_to_cart import add_items_to_cart
import allure
import pytest


# def test_search_amazon(driver):
#     open_amazon_homepage(driver)
#     search_for_product(driver, "laptop")
#     assert "Amazon.in : laptop" in get_search_results_title(driver)
#
#
# def test_get_product_titles(driver):
#     open_amazon_homepage(driver)
#     search_for_product(driver, "laptop")
#     product_titles = get_product_titles(driver)
#     assert len(product_titles) > 0
#     print("First few products titles : ", product_titles[:5])
#     expected_product = "Acer Aspire Lite"
#     assert any(expected_product in title for title in product_titles),f"{expected_product} not found"
#
#
# def test_select_product(driver):
#     open_amazon_homepage(driver)
#     search_for_product(driver, "iphone13+256gb")
#     print(select_product(driver, "iphone"))


@allure.feature('add product to cart')
@allure.story('search and add product to cart')
def test_add_product_to_cart(driver):
    with allure.step('open_amazon_homepage'):
        open_amazon_homepage(driver)
    with allure.step('search for product'):
        search_for_product(driver, "iphone13+256gb")
    print(select_product(driver, "Apple"))
    with allure.step('switch window'):
        switch_window(driver)
    with allure.step('add items to cart'):
        add_items_to_cart(driver)
