import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Detect OS
if platform.system() == "Windows":
    chrome_driver_path = r"C:\Drivers\chromedriver-win64\chromedriver.exe"
    chrome_binary_path = None
else:
    chrome_driver_path = "/usr/bin/chromedriver"
    chrome_binary_path = "/usr/bin/google-chrome"

# Chrome options
options = Options()
if chrome_binary_path:
    options.binary_location = chrome_binary_path
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdQPxfXwDysopvaWiNfzfaAD6hjuFquw-xeGh8TZpMF4roWfQ/viewform")
driver.maximize_window()

# Wait until all input fields are visible
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.whsOnd"))
)
inputs = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input.whsOnd"))
)

inputs[0].send_keys("Taimoor Kamran")
inputs[1].send_keys("Kamran Sattar")
inputs[2].send_keys("12345")
inputs[3].send_keys("37")
inputs[4].send_keys("03413739780")
inputs[5].send_keys("taimoor@gmail.com")

driver.find_element(By.XPATH, '//span[text()="Submit"]').click()

input("Form filled. Press Enter to close browser...")
driver.quit()
