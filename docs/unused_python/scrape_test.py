
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

# Initialize the webdriver and navigate to the page
#driver = webdriver.chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://www.nfl.com/games/49ers-at-seahawks-2022-reg-15")

driver.maximize_window()
driver.implicitly_wait(5)

# Wait for the page to load
#time.sleep(5)

# click cookie button
#cookie_div = driver.find_element(By.XPATH, '//div[@id=''']')

# Find the button element and click it

# other button ive tried
#button = driver.find_element(By.XPATH, "//div[contains(text(), 'Download Game Book (PDF)')]" )
#button = driver.find_element(By.LINK_TEXT, "Download Game Book (PDF)" )
#button = driver.find_element(By.PARTIAL_LINK_TEXT, "Download Game Book (PDF)" )
#button = driver.find_element(By.CLASS_NAME, "css-text-901oao r-alignItems-1awozwy r-color-1khnkhu r-display-6koalj r-flexDirection-18u37iz r-fontFamily-1fdbu1n r-fontSize-1b43r93" )
#button = driver.find_element(By.XPATH, "//button[text(), 'Download Game Book (PDF)']" )

#button = driver.find_element(By.XPATH, "//div[@data-testid='gamecenter-cta-btns-container']" )
#button.click()

# Wait for the PDF to download
#time.sleep(10)

# Get the current URL and print it
#url = driver.current_url
#print(url)

# Close the webdriver
#driver.quit()
