from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver
from selenium import webdriver
from selenium import webdriver

service = FirefoxService("C:\Drivers\geckodriver-v0.34.0-win64\geckodriver.exe")

driver = webdriver.Firefox(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")