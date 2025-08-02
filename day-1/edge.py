from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

service = EdgeService(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "username"))
)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button").send_keys("admin123")