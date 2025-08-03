from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Wait for the search bar to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# Send input using the correct selector
# driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad Carbon Laptop")
# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")
