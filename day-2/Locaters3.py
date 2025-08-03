from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser_obj = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
d = webdriver.Chrome(service=ser_obj)

d.get("https://www.facebook.com/")
d.maximize_window()