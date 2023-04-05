#######################################################
#                  Garrett Marshall                   #
#                                                     #
# Python script that scrapes NFL.com for play-by-play #
# data to be used in spring 2023 data science         #
# capstone project.                                   #
#                                                     #
#######################################################

# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

import re
import requests
from pathlib import Path

#####################################################
#####################################################
# open_site function:
# This funtion takes in a url as a parameter then, 
# opens the site then closes any cookies or pop ups,
# finds all links on page, and then filter out links
# that are not relevent.
# 
def open_site(url):
	# open web site and keep it open
	driver_path = "path/to/chromedriver"
	chr_options = Options()
	chr_options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(driver_path, options=chr_options)

	# open website connection
	driver.get(url)

	# maximize window
	driver.maximize_window()
	driver.implicitly_wait(10)

	# close cookie if it exists
	cookie = driver.find_element(By.XPATH, "//div[@id='onetrust-close-btn-container']")
	if cookie:
		driver.find_element(By.XPATH, "//div[@id='onetrust-close-btn-container']/button" ).click()

	# close drop down menu if it exists
	drop_down = driver.find_element(By.XPATH, "//div[@id='slidedown-footer']")
	if drop_down:
		driver.find_element(By.XPATH, "//button[text()='Later']" ).click()

	# create list of links
	all_links = []

	# identify elements with tagname <a>
	all_links = driver.find_elements(By.TAG_NAME, "a")

	# create game specific links list
	game_links = []

	# traverse list
	for l in all_links:

   		# get_attribute() to get all href
   		link = l.get_attribute("href")

   		# assign game specific links to new list
   		if "games/" in link:

   			# append links
   			game_links.append(link)

	# close window
	driver.quit()

	# return list of game links
	return game_links

##############################################################
##############################################################
# scrape_pdf function:
# this function takes in a url as a parameter
# and scrapes the gamebook pdf off the page,
# then saves the pdf to a folder
def scrape_pdf(url):

    # create pdf url template
    pdf_url = 'https://static.www.nfl.com/gamecenter/{game_id}.pdf'

    # get the html in text format
    html_doc = requests.get(url).text

    # get game_id unique to each game
    game_id = re.search(r"gameID\s*=\s*'([^']+)'", html_doc).group(1)

    # create the pdf url with the game_id
    new_url = pdf_url.format(game_id=game_id)

    # download pdf from pdf link
    response = requests.get(new_url)

    # generate name of pdf
    pdf_name = url[26:]
    pdf_name = pdf_name.replace("-", "_") + ".pdf"

    # save to pdf folder
    with open('/Users/garrett/Desktop/game_book_pdfs/' + pdf_name, 'wb') as f:
        f.write(response.content)
##############################################################
##############################################################

# create link format for the regular season
link_format = "https://www.nfl.com/schedules/2022/REG{week}/"

# begin loop through regular season weeks
for w in range(1,18):

	# get url for specific week
	url = link_format.format(week=w)
	
	# open site and get links of all 
	# completed games on page
	game_links = open_site(url)

	# loop through list of links and download 
	# the Game Book pdf to folder
	for l in game_links:

		# get pdfs
		scrape_pdf(l)




# create link format for the post season
#link_format_post = "https://www.nfl.com/schedules/2022/POST{week}/"

# begin loop through post season weeks
#for w in range(1,5):

	# get url for specific week
	#url = link_format_post.format(week=w)

	# begin loop through all games in week
		# use the href to get link to game page

		# get game book pdf from each game page

		# write pdf to folder


# convert all .pdf to .txt



#driver.implicitly_wait(3)
#driver.quit()









