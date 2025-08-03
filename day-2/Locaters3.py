from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser_obj = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
d = webdriver.Chrome(service=ser_obj)

d.get("https://www.facebook.com/")
d.maximize_window()

WebDriverWait(d, 10).until(
    EC.visibility_of_element_located((By.ID, "email"))
)

# Tag and ID 

# d.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
# d.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# Tag and Class 

# d.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
# d.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")


d.find_element(By.CSS_SELECTOR, "input[data-testid=royal-pass]").send_keys("abc@gmail.com")

