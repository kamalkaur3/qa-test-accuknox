import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://a703594c6d7304517a5d973d121a8e92-1440867682.us-east-2.elb.amazonaws.com/"

response = requests.get(url)
status_code = response.status_code
expected_status_code = 200

if status_code == expected_status_code:
    print(f"Success: Status code is {status_code}.")
else:
    print(f"Failure: Expected status code {expected_status_code}, but got {status_code}.")

# Verify h1 tag
if status_code == expected_status_code:

    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(10)

    element = driver.find_element(By.TAG_NAME, 'h1')
    time.sleep(5)
    element_txt= element.text

    expected_text = 'Hello from the Backend!'

    # Verify if the h1 text matches the expected text
    if element_txt == expected_text:
        print('Success: The h1 tag text matches the backend output.')
    else:
        print(f'Failure: Expected "{expected_text}" but found "{element_txt}".')
    driver.quit()

