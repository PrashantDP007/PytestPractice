
import pytest
import allure
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # Execute the actual test
    outcome = yield
    report = outcome.get_result()

    # Take screenshot only when test fails
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            screenshot = driver.get_screenshot_as_png()

            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )