from amazon.search import search_for_product, get_search_results_title, get_product_titles, select_product, switch_window
from amazon.navigation import open_amazon_homepage
from amazon.add_item_to_cart import add_items_to_cart
import allure


@allure.feature('search functionality')
@allure.description('search for a product')
@allure.testcase("search a product")
def test_select_product(driver):
    with allure.step('open_amazon_homepage'):
        open_amazon_homepage(driver)
    with allure.step('search for product'):
        search_for_product(driver, "iphone13+256gb")
        print(select_product(driver, "iphone"))

@allure.feature('search functionality')
@allure.description('search for a product and validate the page title')
@allure.testcase("search and add a product to cart")
def test_search_amazon(driver):
    with allure.step('open_amazon_homepage'):
        open_amazon_homepage(driver)
    with allure.step('search for product'):
        search_for_product(driver, "laptop")
    with allure.step('add an assertion'):
        assert "Amazon.in : laptop" in get_search_results_title(driver)


@allure.feature('search functionality')
@allure.description('below test will search for a product, get product list and validate if product is present in the result')
@allure.testcase("search and verify the result")
def test_get_product_titles(driver):
    with allure.step('open_amazon_homepage'):
        open_amazon_homepage(driver)
    with allure.step('search for product'):
        search_for_product(driver, "laptop")
    with allure.step('retrieve the product titles'):
        product_titles = get_product_titles(driver)
    with allure.step('add an assertion to validate the results are returned'):
        assert len(product_titles) > 0
    with allure.step('print first few titles of the result'):
        print("First few products titles : ", product_titles[:5])
    with allure.step('product name to be validated'):
        expected_product = "Acer Aspire Lite"
    with allure.step('add an assertion to validate the expected product is present in the result'):
        assert any(expected_product in title for title in product_titles),f"{expected_product} not found"

@allure.feature('search functionality')
@allure.description('search for a product')
@allure.testcase("search and add a product to cart")
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



#





