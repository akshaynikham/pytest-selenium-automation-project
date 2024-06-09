from amazon.search import search_for_product, get_search_results_title, get_product_titles,select_product
from amazon.navigation import open_amazon_homepage


# def test_search_amazon(driver):
#     open_amazon_homepage(driver)
#     search_for_product(driver, "laptop")
#     assert "Amazon.in : laptop" in get_search_result_title(driver)


# def test_get_product_titles(driver):
#     open_amazon_homepage(driver)
#     search_for_product(driver, "laptop")
#     product_titles = get_product_titles(driver)
#     assert len(product_titles) > 0
#     print("First few products titles : ", product_titles[:5])
#     expected_product = "Acer Aspire Lite"
#     assert any(expected_product in title for title in product_titles),f"{expected_product} not found"


def test_select_product(driver):
    open_amazon_homepage(driver)
    search_for_product(driver, "laptop")
    print(select_product(driver, "HP"))




