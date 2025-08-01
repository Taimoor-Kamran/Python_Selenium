# 1) Open Web Browser(Chrome/firefox/IE).
# 2) Open URL https://opensource.demo.orangehrmlive.com/
# 3) provide Email (admin@yourstore.com).
# 4) Provide Password (admin).
# 5) Click on Login.
# 6) Capture title of the dashboard page.(Actual title)
# 7) Verify tilte of the page: "Dashboard / nopCommerce administration" (Exected)
# 8) close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

