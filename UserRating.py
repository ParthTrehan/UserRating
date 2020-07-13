from bs4 import BeautifulSoup
import requests
import argparse
import re

from RatingCalulator import calculate

def airbnb_regex_type(argValue, pat=re.compile(r"(https?:\/\/)(www\.)airbnb.com\/users\/show\/([0-9]+)")):
    if not pat.match(argValue):
        raise argparse.ArgumentTypeError('Please enter a vaild Airbnb user URL')
    return argValue

def run(args):
    try:
        url=args.url
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        divs = soup.findAll("div", {"data-veloute": "user_profile_frame"})
        if len(divs)>0:
            reviewsParent = soup.findAll("h2", {"id": "review-section-title"})[0]
            reviewsDiv = reviewsParent.findAll("div", {"class": "_1p0spma2"})[0]
            numberOfReviews = int(reviewsDiv.text.split(' ')[0])
            percentile = calculate(numberOfReviews)
            if percentile<100.0 and percentile>0.00:
                topPercent = round((100-percentile), 2)
                print(args.url,'is in the top',topPercent,'of Melbourne Airbnb users based on number of reviews')
            elif percentile==100.0:
                print(args.url, 'has the highest number of reviews based on number of of Melbourne Airbnb users reviews')
        else:
            print('The user data cannnot be extracted as the user is private')

    except Exception:
        print('There was an error extracting the airbnb user data. Please try again later.')

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=airbnb_regex_type,required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()
    run(args)