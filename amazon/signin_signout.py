from selenium.webdriver.common.by import By


def signIn_signOut(driver):
    signIn = driver.find_element(By.ID, "" )
    signIn.click()
    driver.implicitly_wait(10)
