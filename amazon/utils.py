from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def initialize_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

def switch_window(driver):
    original_window = driver.current_window_handle
    print(f"original window handle: {original_window}")
    all_windows = driver.window_handles
    print(f"all handles : {all_windows}")
    driver.switch_to.window(all_windows[-1])


def hover_and_select(driver, hover_locator, select_locator):
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)
    hover_element = wait.until(EC.presence_of_element_located((hover_locator)))
    actions.move_to_element(hover_element).perform()
    select_element = wait.until(EC.element_to_be_clickable((select_locator)))
    select_element.click()


def is_logged_in(driver):
    try:
        account_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nav-link-accountList-nav-line-1'))).text
        return "Hello, Sanjana" in account_name
    except:
        return False


def is_logged_out(driver):
    try:
        account_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Sign in']"))).text
        return "Sign in" in account_name
    except:
        return False
