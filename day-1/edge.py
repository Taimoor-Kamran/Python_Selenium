from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = EdgeService(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Wait for username field
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "username"))
)

# Perform login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for dashboard to load
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "oxd-topbar-header-userarea"))
)

print("Login successful")
driver.quit()
