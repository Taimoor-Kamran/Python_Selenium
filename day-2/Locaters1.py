from selenium import webdriver
from selenium.webdriver.common.service import Service

ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(ser_obj)
