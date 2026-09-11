
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox") # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems

    driver = webdriver.Chrome(options=chrome_options) # Initialize the Chrome WebDriver with the specified options
    
    yield driver # Provide the driver to the test function

    driver.quit() # Clean up and close the browser after the test is done