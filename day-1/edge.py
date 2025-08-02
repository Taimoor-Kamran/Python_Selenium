from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

service = EdgeService(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

WebDriverWait(driver, 10).until(
    
)

driver.get("https://opensource-demo.orangehrmlive.com/")
