from selenium import webdriver
from selenium.webdriver.common.service import Service

service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)
