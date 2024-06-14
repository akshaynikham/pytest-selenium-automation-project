from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def search_for_product(driver, product_name):
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)


def get_search_results_title(driver):
    return driver.title


def get_product_elements(driver):
    return driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")


def get_product_titles(driver):
    elements = get_product_elements(driver)
    return [element.text for element in elements]


def select_product(driver, product_title):
    products = get_product_elements(driver)

    if product_title:
        for product in products:
            if product_title in product.text:
                product.click()
                return product.text
        raise Exception(f"Product with title '{product_title}' not found.")
    else:
        # Select the first product if no specific title is provided
        if products:
            products[0].click()
            return products[0].text
        else:
            raise Exception("No products found on the page.")


def switch_window(driver):
    original_window = driver.current_window_handle
    print(f"original window handle: {original_window}")
    all_windows = driver.window_handles
    print(f"all handles : {all_windows}")
    driver.switch_to.window(all_windows[-1])
    # for window in all_windows:
    #     if window != original_window:
    #         print(f"window switched successfully")
    #         driver.switch_to.window(window)
    #         break
