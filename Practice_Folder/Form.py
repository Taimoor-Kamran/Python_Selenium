from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=ser_obj)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdQPxfXwDysopvaWiNfzfaAD6hjuFquw-xeGh8TZpMF4roWfQ/viewform")

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input.whsOnd"))
)

input = driver.find_element(By.CSS_SELECTOR, 'input.whsOnd')
