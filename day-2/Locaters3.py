from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
