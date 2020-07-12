# importing the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import time
from collections import defaultdict
import os
import glob

start = time.time()
reviewersDict = dict()
Users = pd.read_csv('UserIDs.CSV')
for review in Users.UniqueId:
    try:
        url='https://www.airbnb.com.au/users/show/'+str(review)
        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(url).text
        # Parse the html content
        soup = BeautifulSoup(html_content, "lxml")
        divs = soup.findAll("div", {"class": "_1ekkhy94"})
        if len(divs)>0:
            reviewsParent = soup.findAll("h2", {"id": "review-section-title"})[0]
            reviewsDiv = reviewsParent.findAll("div", {"class": "_1p0spma2"})[0]
            locationDiv = soup.findAll("div", {"class": "_910j1c5"})[0]
            if 'Lives in' in locationDiv.text:
                reviewersDict[review] = {
                    "Number of reviews":int(reviewsDiv.text.split(' ')[0]),
                    "Location":str(locationDiv.text.split("Lives in ")[1])
                }
    except Exception:
        continue
print(time.time()-start)
pd.DataFrame.from_dict(reviewersDict,orient='index').to_csv('airbnbUsers.csv')