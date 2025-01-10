#
# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
# # Configuration for the browser driver
# BROWSER = "chrome"  # Change to "firefox" if you prefer
#
# @pytest.fixture(scope="module")
# def driver():
#     """Setup Selenium WebDriver."""
#     if BROWSER.lower() == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif BROWSER.lower() == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     else:
#         raise ValueError("Unsupported browser!")
#
#     # Maximize the browser window
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# def test_search_functionality(driver):
#     """Test the search functionality on Selenium Playground."""
#     # Navigate to the Selenium Playground Table Search Demo
#     url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
#     driver.get(url)
#
#     # Locate the search box and input "New York"
#     search_box = driver.find_element(By.XPATH, "//*[@id='example_filter']/label/input")
#     search_query = "New York"
#     search_box.clear()
#     search_box.send_keys(search_query)
#
#     # Wait for 10 seconds to observe the result
#     time.sleep(10)
#
#
#
#     # Wait to observe the scroll effect
#     time.sleep(2)
#
#     # Validate the search results
#     rows = driver.find_elements(By.XPATH, "//*[@id='example']/tbody/tr")
#     visible_rows = [row for row in rows if row.is_displayed()]
#
#
#
#     # # Assert that at least one row is visible with the search query
#     # assert len(visible_rows) > 0, "No rows found for the search query."
#     driver.execute_script("window.scrollTo(0, 0);")
#
#
#     # Print the rows for debugging purposes
#     for row in visible_rows:
#         print(row.text)
#
#
#
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

# Configuration for the browser driver
BROWSER = "chrome"  # Change to "firefox" if you prefer

@pytest.fixture(scope="module")
def driver():
    """Setup Selenium WebDriver."""
    if BROWSER.lower() == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif BROWSER.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Unsupported browser!")

    # Maximize the browser window
    driver.maximize_window()
    yield driver
    driver.quit()

def test_search_functionality(driver):
    """Test the search functionality on Selenium Playground."""
    # Navigate to the Selenium Playground Table Search Demo
    url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    driver.get(url)

    # Locate the search box and input "New York"
    search_box = driver.find_element(By.XPATH, "//*[@id='example_filter']/label/input")
    search_query = "New York"
    search_box.clear()
    search_box.send_keys(search_query)

    # Wait for 10 seconds to observe the result
    time.sleep(10)

   
    # Validate the search results
    rows = driver.find_elements(By.XPATH, "//*[@id='example']/tbody/tr")
    visible_rows = [row for row in rows if row.is_displayed()]

    # Assert that at least one row is visible with the search query
    assert len(visible_rows) > 0, "No rows found for the search query."

    # Print the rows for debugging purposes
    for row in visible_rows:
        print(row.text)
