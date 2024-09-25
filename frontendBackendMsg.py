import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Pytest fixture for WebDriver setup
@pytest.fixture(scope="module")
def setup_driver():
    driver = webdriver.Chrome()
    driver.get("https://marketplace.digital-arms.com/")
    driver.maximize_window()
    time.sleep(10)
    driver.quit()

# Test function for searching and verifying error message
def test_search_something_and_verify_error_message(setup_driver):
    driver = setup_driver

    # Search for an invalid item
    driver.find_element(By.XPATH, '//input[@placeholder="Search item here..."]').send_keys("gsfjsdf")
    time.sleep(5)

    # Get the displayed message after search
    displayed_msg = driver.find_element(By.XPATH, '/html/body/div/header/nav/div/div/div[2]').text
    expected_msg = "No Result Found"

    # Assertion to verify the message
    assert displayed_msg == expected_msg, f"The message displayed ({displayed_msg}) does not match the expected message ({expected_msg})!"
