from selenium import webdriver


def initialize_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver
