from selenium.common import ElementClickInterceptedException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def apply_delivery_filter(driver, option_text, max_attempt = 3):
        filter_xpath = f"//div[@id='deliveryRefinements']//li[.//span[contains(text(), '{option_text}')]]//input[@type='checkbox']"
        wait = WebDriverWait(driver, 15)
        checkbox = wait.until(EC.presence_of_element_located((By.XPATH, filter_xpath)))
        retries = 0
        while retries < max_attempt:
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
                    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, filter_xpath)))

                    if not checkbox.is_selected():
                        driver.execute_script("arguments[0].click()", checkbox)

                    wait.until(EC.staleness_of(checkbox))

                except TimeoutException:
                    break

                except StaleElementReferenceException:
                    retries+=1
                    continue

        checkbox = wait.until(EC.presence_of_element_located((By.XPATH, filter_xpath)))
        assert checkbox.is_selected(), "The checkbox is not selected"
        # results = wait.until(EC.presence_of_element_located((By.ID, "search")))
        results = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")))
        for result in results:
            return results[0].click()
            # return print(f"items selected"


# def apply_delivery_filter(driver):
#     wait = WebDriverWait(driver, 15)
#     filter_locator = "//div[@id='deliveryRefinements']//li[@aria-label='Get It in 2 Days']"
#     Get_It_Today_Button = wait.until(EC.element_to_be_clickable((By.XPATH, f"{filter_locator}")))
#     Get_It_Today_Button.click()
#     time.sleep(5)

# def apply_delivery_filter(driver, option_text):
#     filter_xpath = f"//div[@id='deliveryRefinements']//li[.//span[contains(text(), '{option_text}')]]//input[@type='checkbox']"
#     wait = WebDriverWait(driver, 10)
#     checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, filter_xpath)))
#     checkbox.click()


# def apply_delivery_filter(driver, option_text, max_retries = 5):
#     filter_xpath = f"//div[@id='deliveryRefinements']//li[.//span[contains(text(), '{option_text}')]]//input[@type='checkbox']"
#     wait = WebDriverWait(driver, 10)
#     retries = 0
#     while retries < max_retries:
#
#         try:
#
#             checkbox = wait.until(EC.presence_of_element_located((By.XPATH, filter_xpath)))
#             driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
#             checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, filter_xpath)))
#             driver.execute_script("arguments[0].click();", checkbox)
#             is_selected = driver.execute_script("return arguments[0].checked;", checkbox)
#
#             if is_selected:
#                 break
#             else:
#                 raise Exception(f"checkbox for {option_text} was not selected")
#
#         except (StaleElementReferenceException, ElementClickInterceptedException) as e:
#             print(f"Exception caught: {e}, retrying...")
#             retries += 1
#
#     if retries == max_retries:
#         raise Exception(f"Failed to apply filter for {option_text} after {max_retries} attempts")
#
#     wait.until(EC.presence_of_element_located((By.ID, "search")))
#
#     results_xpath = f"//span[contains(text(), '{option_text}')]"
#     results = driver.find_elements(By.XPATH, results_xpath)
#
#     assert len(results) > 0, f"No results found for {option_text}"
#     print(f"Filter {option_text} applied successfully with {len(results)} results.")

# def apply_brand_filter(driver, Brand_name):
#     wait = WebDriverWait(driver, 15)
#     filter_locator = f"//div[@id='brandsRefinements']//li[contains(@aria-label, '{Brand_name}')]//input[@type='checkbox']"
#     print(f"{filter_locator}")
#     see_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='See more']")))
#     see_more_button.click()
#     checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, filter_locator)))
#     print(checkbox)
#     # checkbox = driver.find_element(By.XPATH, filter_locator)
#     # time.sleep(10)
#     checkbox.click()

