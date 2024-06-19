import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from amazon.utils import hover_and_select, is_logged_in, is_logged_out

load_dotenv()
USERNAME = os.getenv("AMAZON_USERNAME")
PASSWORD = os.getenv("AMAZON_PASSWORD")


def login(driver):
    # USERNAME = os.getenv("AMAZON_USERNAME")
    # PASSWORD = os.getenv("AMAZON_PASSWORD")

    assert not is_logged_in(driver), "user already logged-in"

    print(f"{USERNAME}")
    login = driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
    login.click()
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.element_to_be_clickable((By.ID, "ap_email")))
    username_field.click()
    username_field.clear()
    username_field.send_keys(USERNAME)
    continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    continue_button.click()
    password_field = wait.until(EC.element_to_be_clickable((By.ID, 'ap_password')))
    password_field.clear()
    password_field.click()
    password_field.send_keys(PASSWORD)
    signin_button = wait.until(EC.element_to_be_clickable((By.ID, 'signInSubmit')))
    signin_button.click()
    account_name = wait.until(EC.presence_of_element_located((By.ID, 'nav-link-accountList-nav-line-1')))
    assert "Hello, Sanjana" in account_name.text, "Login failed"

def logout(driver):
    assert is_logged_in(driver), "user logged-in"
    hover_locator = (By.ID, "nav-link-accountList")
    select_locator = (By.ID, "nav-item-signout")
    hover_and_select(driver, hover_locator, select_locator)
    assert is_logged_out(driver), "user not logged-out"





