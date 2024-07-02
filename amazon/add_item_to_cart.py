from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_items_to_cart(driver):

    wait = WebDriverWait(driver, 20)
    add_to_cart = "//input[@id='add-to-cart-button'][@type='submit']"
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart)))
    driver.execute_script("arguments[0].click();", add_to_cart_button)
    assert "Added to Cart" in driver.page_source, "item was not added"


    # try:
    #
    #     add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
    # except TimeoutException:
    #     print("Add to Cart button not found by ID. Trying XPath.")
    #     try:
    #
    #         add_to_cart_button = wait.until(
    #             EC.element_to_be_clickable((By.XPATH, "//input[@id='add-to-cart-button'][@type='submit']")))
    #     except TimeoutException:
    #         print("Add to Cart button not found by XPath. Trying CSS Selector.")
    #         try:
    #
    #             add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    #                                                                         "div[class='a-section a-spacing-none a-padding-none'] div[id='addToCart_feature_div'] div[class='a-button-stack']")))
    #         except TimeoutException:
    #             print("Add to Cart button not found by CSS Selector. Raising exception.")
    #             raise