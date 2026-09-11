from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get('https://www.google.com')

# driver.find_element(By.XPATH, "//textarea[contains(@jsname,'yZiJ')]").clear()
# driver.find_element(By.XPATH, "//textarea[contains(@jsname,'yZiJ')]").send_keys("Prashant Pardeshi")
# driver.find_element(By.XPATH, "//div[@jsname='VlcLAe']//input[@value = 'Google Search']").click() # need wait ElementNotInteractableException exception



# # After explicit wait
# driver.get('https://www.google.com')
# driver.find_element(By.XPATH, "//textarea[contains(@jsname,'yZiJ')]").clear()
# driver.find_element(By.XPATH, "//textarea[contains(@jsname,'yZiJ')]").send_keys("Prashant Pardeshi")

# search_locator = (By.XPATH, "//div[@jsname='VlcLAe']//input[@value='Google Search']")

# search = wait.until(EC.visibility_of_element_located(search_locator)) # after explicit wait
# search.click()


# driver.back()
# driver.forward()
# driver.get("https://github.com") # new url with same tab
# parent = driver.current_window_handle # git
# driver.close()
# # 2️⃣ Same driver → open new tab ✅
# driver.execute_script("window.open('https://google.com','_blank');")

# driver.switch_to.window(driver.window_handles[0]) # git
# driver.switch_to.window(driver.window_handles[1]) # google
# driver.switch_to.window(parent) # git

# # 4️⃣ Open a new tab / window
# # New Tab
# driver.switch_to.new_window('tab')
# driver.get("https://www.facebook.com/")

# driver.switch_to.window(driver.window_handles[0]) # git
# driver.switch_to.window(driver.window_handles[1]) # google
# driver.switch_to.window(driver.window_handles[2]) # facebbok

def test_google_search(driver):
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.google.com')
    driver.find_element(By.XPATH, "//textarea[contains(@jsname,'yZiJ')]").clear()
    driver.find_element(By.XPATH, "//textarea[contains(@jsname,'yZiJ')]").send_keys("Prashant Pardeshi")

    search_locator = (By.XPATH, "//div[@jsname='VlcLAe']//input[@value='Google Search']")

    search = wait.until(EC.visibility_of_element_located(search_locator)) # after explicit wait
    search.click()

