from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to geckodriver
service = FirefoxService(r"C:\Drivers\geckodriver-v0.34.0-win64\geckodriver.exe")
driver = webdriver.Firefox(service=service)

# Open URL
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Wait until username input is visible (max 10 seconds)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "username"))
)

# Now login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Optional: wait to see dashboard
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "oxd-topbar-header-userarea"))
)

print("Login successful")
driver.quit()
