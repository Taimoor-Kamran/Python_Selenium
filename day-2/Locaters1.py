from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=ser_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.NAME, "small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")
driver.find_element(By.ID, "q").send_keys("Lenovo Thinkpad Carbon Laptop")
