from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

service = FirefoxService(r"C:\Drivers\geckodriver-v0.34.0-win64\geckodriver.exe")
driver = webdriver.Firefox(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

