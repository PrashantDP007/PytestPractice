from selenium.webdriver.common.by import By
import requests

# test case to test the links un pages are not broken and working fine 
def test_links(driver):
    driver.get("https://www.google.com/")
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Total links found: {len(links)}")
    print(f"LInks are: {[link.get_attribute('href') for link in links]}")
    for link in links:
        url = link.get_attribute("href")
        print(f"Testing link: {url}")
        if url:
            response = requests.head(url)
            assert response.status_code == 200, f"Broken link: {url} with status code: {response.status_code}"

# test window switching functionality
def test_window_switching(driver):
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_open")
    driver.switch_to.frame("iframeResult")
    driver.find_element(By.TAG_NAME, "button").click()

    main_window = driver.current_window_handle 
    all_windows = driver.window_handles # get all window handles
    for window in all_windows:
        if window != main_window: # check if the window is not the main window
            driver.switch_to.window(window) # switch to the new window
            print(f"Switched to new window with title: {driver.title}") 
            driver.close()
            break
    driver.switch_to.window(main_window)
    print(f"Switched back to main window with title: {driver.title}")