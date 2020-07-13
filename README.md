# Airbnb user's Relative Ranking Calculater
This is a simple service that extracts airbnb user's Relative Ranking from the user's profile URL. The calculation is based on the number of reviews the user has and how relative it is based on the melbourne airbnb users data. The repository also contains data scraping tool that extracts the airbnb user data based on data curated by <a href="http://insideairbnb.com/get-the-data.html" target="_blank">Insider Airbnb</a>.

## Table of Contents (Optional)

- [Files](#files)
- [Installation](#installation)
- [Packages](#packages)


---

## CLI Example

```bash
# CLI command
python UserRating.py --url https://www.airbnb.com/users/show/3954907
# Output would be like
"https://www.airbnb.com/users/show/99824610 is in the top 77.17 of Melbourne Airbnb users based on number of reviews"
```
---

## Files
- [UserReviewsScraper.py](https://github.com/ParthTrehan/UserRating/blob/master/UserReviewsScraper.py "UserReviewsScraper.py") - This is a Airbnb user data scraping python script. It uses a list of Airbnb users Unique IDs and extract the number of reviews the user has and the location of that user shown on Airbnb user profile. This scripts does not extracts private user data but only extracts the user's data if the user profile is public. This script saves two CSV files that are 
	1. [UserIDs.CSV](https://github.com/ParthTrehan/UserRating/blob/master/UserIDs.CSV "UserIDs.CSV") - This file contains the list of airbnb users who have lived in melbourne based on data given by <a href="http://insideairbnb.com/get-the-data.html" target="_blank">Insider Airbnb</a>.
	2. [Melbourne_airbnb_users.csv](https://github.com/ParthTrehan/UserRating/blob/master/Melbourne_airbnb_users.csv "Melbourne_airbnb_users.csv")  -   his file contains the list of airbnb users who are melbourne based and  have lived in melbourne based on data given by <a href="http://insideairbnb.com/get-the-data.html" target="_blank">Insider Airbnb</a>.
	
- [UserRating.py](https://github.com/ParthTrehan/UserRating/blob/master/UserRating.py "UserRating.py") - This is the main file that parses command line argument to extract a particular user data from airbnb and also extracts the number of reviews the user has.
- [RatingCalulator.py](https://github.com/ParthTrehan/UserRating/blob/master/RatingCalulator.py "RatingCalulator.py") -  This is the file that calculates percentile of a given user based on the data extracted in [Melbourne_airbnb_users.csv](https://github.com/ParthTrehan/UserRating/blob/master/Melbourne_airbnb_users.csv "Melbourne_airbnb_users.csv"). 

## Installation

- All the `code` is available in this repo to get started

### Clone

- Clone this repo to your local machine using `https://github.com/ParthTrehan/UserRating.git`

### Setup

> update and install this package first

```bash
pip install -r requirements.txt
```

> now just use bash to use the service as shown
```bash
#code away!
python UserRating.py --url https://www.airbnb.com/users/show/3954907
```

## Packages

- <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">Beautiful Soup</a>
- <a href="https://requests.readthedocs.io/en/master/" target="_blank">Requests</a>
- <a href="https://pandas.pydata.org/" target="_blank">Pandas</a>
- <a href="https://www.scipy.org/" target="_blank">SciPy</a>

