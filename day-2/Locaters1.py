from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(ser_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.ID, "small-searchterms")