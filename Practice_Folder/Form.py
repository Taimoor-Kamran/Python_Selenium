from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup ChromeDriver
service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdQPxfXwDysopvaWiNfzfaAD6hjuFquw-xeGh8TZpMF4roWfQ/viewform")
driver.maximize_window()

# Wait until the first input field is visible
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input.whsOnd"))
)

# Find and fill all input fields
inputs = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd")

inputs[0].send_keys("Taimoor Kamran")        # Full Name
inputs[1].send_keys("Kamran Sattar")         # Father Name
inputs[2].send_keys("12345")                 # ID
inputs[3].send_keys("37")                    # Age or Roll No.
inputs[4].send_keys("03413739780")           # Phone
inputs[5].send_keys("taimoor@gmail.com")     # Email

driver.find_element(By.XPATH, '//span[text()="Submit"]').click()

input("Form filled. Press Enter to close browser...")

driver.quit()
