import pandas as pd
from scipy import stats

def calculate(score):
    melbUsers = pd.read_csv('Melbourne_airbnb_users.csv')
    reviewsArr = melbUsers['Number of reviews'].to_numpy()
    percentile = stats.percentileofscore(reviewsArr, score)
    return percentile