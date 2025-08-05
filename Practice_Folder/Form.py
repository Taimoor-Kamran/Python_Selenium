import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set platform-specific ChromeDriver path
if platform.system() == "Windows":
    chrome_driver_path = r"C:\Drivers\chromedriver-win64\chromedriver.exe"
else:
    chrome_driver_path = "/usr/bin/chromedriver"

# Create WebDriver service
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the Google Form
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdQPxfXwDysopvaWiNfzfaAD6hjuFquw-xeGh8TZpMF4roWfQ/viewform")
driver.maximize_window()

# Wait until all form fields are present
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.whsOnd"))
)

inputs = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd")

# Fill the form
if len(inputs) >= 6:
    inputs[0].send_keys("Taimoor Kamran")
    inputs[1].send_keys("Kamran Sattar")
    inputs[2].send_keys("12345")
    inputs[3].send_keys("37")
    inputs[4].send_keys("03413739780")
    inputs[5].send_keys("taimoor@gmail.com")

    # Submit the form
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Submit"]'))
    ).click()

    print("✅ Form submitted successfully.")
else:
    print("❌ Not enough input fields found.")

# Optional for local dev: pause before closing browser
if platform.system() == "Windows":
    input("Press Enter to close browser...")

driver.quit()
