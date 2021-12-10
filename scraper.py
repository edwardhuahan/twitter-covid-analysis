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


# need to set the tweets somewhere
tweets_lst = []

# scrape data
for i, tweet in enumerate(snt.TwitterSearchScraper('Covid' or 'shitting').get_items()):
    if i > 100:
        break
    tweets_lst.append([tweet.id, tweet.date, tweet.content])

# creating dataframe
tweets_df = pd.DataFrame(tweets_lst, columns=['Tweet Id', 'Datetime', 'Text'])
tweets_df.to_csv(sep=',', index=False)
