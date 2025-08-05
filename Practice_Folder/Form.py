from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdQPxfXwDysopvaWiNfzfaAD6hjuFquw-xeGh8TZpMF4roWfQ/viewform")
driver.maximize_window()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input.whsOnd"))
)

inputs = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd")

inputs[0].send_keys("Taimoor Kamran")         
inputs[1].send_keys("Kamran Sattar")          
inputs[2].send_keys("12345")                 
inputs[3].send_keys("37")                     
inputs[4].send_keys("03413739780")           
inputs[5].send_keys("taimoor@gmail.com")     

driver.find_element(By.XPATH, '//span[text()="Submit"]').click()

input("Form filled. Press Enter to close browser...")

driver.quit()
