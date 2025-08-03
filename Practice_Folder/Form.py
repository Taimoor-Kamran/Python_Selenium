from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdQPxfXwDysopvaWiNfzfaAD6hjuFquw-xeGh8TZpMF4roWfQ/viewform")
driver.maximize_window()

inputs = driver.find_element(By.CSS_SELECTOR, "input.whsOnd")

inputs[0].send_keys("Taimoor Kamran")
inputs[1].send_keys("Kamran Sattar")
inputs[2].send_keys("12345")
inputs[3].send_keys("03413739780")
inputs[4].send_keys("taimoor@gmail.com")
