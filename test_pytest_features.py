from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()


# Click SECOND product using find_elements
products = driver.find_elements(By.CLASS_NAME, "inventory_item")

# 👉 Clicks 2nd product’s “Add to cart” button
products[1].find_element(By.TAG_NAME,"button").click()

# Checking commits