# 1) Open Web Browser(Chrome/firefox/IE).
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) provide Email (admin@yourstore.com).
# 4) Provide Password (admin).
# 5) Click on Login.
# 6) Capture title of the dashboard page.(Actual title)
# 7) Verify tilte of the page: "Dashboard / nopCommerce administration" (Exected)
# 8) close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup ChromeDriver
service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open OrangeHRM demo site
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Wait for username field to appear
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "username"))
)

# Fill login form
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
act_title=driver.title
exp_title="OrangeHRM"
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

# Wait to visually confirm login
time.sleep(10)

# Close browser
driver.quit()
