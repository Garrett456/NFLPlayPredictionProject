#################################################
#
# This script scrapes and downloads 
# nfl game books off of each nfl game website
#
################################################

# load libraries
import re
import requests
from pathlib import Path

# get url of game
url = 'https://www.nfl.com/games/colts-at-broncos-2022-reg-5'

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
    with open('/Users/garrett/Desktop/nfl_urls/' + pdf_name, 'wb') as f:
        f.write(response.content)
##############################################################

scrape_pdf(url)






