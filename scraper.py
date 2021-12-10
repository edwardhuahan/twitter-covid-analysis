"""
DEC 09 2021

This script is used to scrape tweets from twitter for use in my csc110 final project
The scraper accepts a range of dates and outputs the tweets into a csv file.
Each line of data in the csv file will be of the following:
<status id>, <status date>, <content>

This scraper uses the snscraper and pandas libraries.
"""

import snscrape.modules.twitter as snt
import pandas as pd
import numpy as np
import csv
import datetime as dt
import time

from datetime import datetime, timedelta
now = datetime.now()
now = now.strftime('%Y-%m-%d')

max_tweets = 100

# setting up the csv file and writer
# open csv file, make new one if file not found
csvFile = open('scraper-output/scrapes.csv', mode='a', newline='', encoding='utf8')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id', 'date', 'contents', ])

# need to set the tweets somewhere
tweets_lst = []

# scrape data
for i, tweet in enumerate(snt.TwitterSearchScraper('Covid' or 'shitting').get_items()):
    if i > 10:
        break
    tweets_lst.append([tweet.id, tweet.date, tweet.content])

# creating dataframe
tweets_df = pd.DataFrame(tweets_lst, columns=['Tweet Id', 'Datetime', 'Text'])
tweets_df.to_csv(path_or_buf=None, sep=',', index=False)
