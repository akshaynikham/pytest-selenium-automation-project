from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def open_amazon_homepage(driver):
    driver.get("https://www.amazon.in")

