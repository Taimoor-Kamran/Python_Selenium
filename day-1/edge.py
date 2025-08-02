from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

service = EdgeService(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")

driver = webdriver.Edge(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")
