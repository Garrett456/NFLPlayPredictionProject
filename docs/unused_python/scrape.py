# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome (executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.nfl.com/schedules/2022/REG1/")

links = []

# identify elements with tagname <a>
links = driver.find_elements(By.TAG_NAME, "a")

links2 = []

# traverse list
for l in links:
   # get_attribute() to get all href
   link = l.get_attribute("href")

   if "games/" in link:
        links2.append(link)

driver.quit()

links2 = list(set(links2))

print(links2)

print(len(links2))








