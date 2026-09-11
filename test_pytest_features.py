from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

print("Test copilotr features working fine")

# create python code to reverse string 
def reverse_string(s):
    return s[::-1]

# create python code to check if a number is prime 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# I want to scroll and click the selenium element using python code
from selenium.webdriver.common.action_chains import ActionChains
element = driver.find_element(By.ID, "some-element-id")
actions = ActionChains(driver)
actions.move_to_element(element).click().perform()


# ✅ BEST PRACTICE #1: Scroll ONLY to the element (Amazon-safe)
# 🔥 Industry-standard solution


driver.get("https://www.amazon.in")

# Search product
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphone 15")
driver.find_element(By.ID, "nav-search-submit-button").click()

# Wait for search results
wait = WebDriverWait(driver, 15)
product = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[text()='22,999']")
    )
)

# Scroll to product
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", product) 

# Click safely
wait.until(EC.element_to_be_clickable(product)).click()

# create a function to wait until element is visible and then click it by passing locator as argument
def wait_and_click(locator):
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.visibility_of_element_located(locator))
    element.click()


