from selenium import webdriver
from selenium.webdriver.common.service import Service

service = Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")

driver = webdriver.Edge(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")