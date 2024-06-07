from amazon.search import open_amazon_homepage


def test_search_amazon(driver):
    open_amazon_homepage(driver)


# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()


# def test_google_search(setup):
#     driver = setup
#     driver.get("https://www.google.com")
#     assert "Google" in driver.title
#     search_box = driver.find_element(By.NAME, "q")
#     search_box.send_keys("Selenium")
#     search_box.submit()
#     assert "Selenium" in driver.page_source
