import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://marketplace.digital-arms.com/")
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
