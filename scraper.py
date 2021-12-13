"""
DEC 09 2021

This script is used to scrape tweets from twitter for use in my csc110 final project
The scraper accepts a range of dates and outputs the tweets into a csv file.
Each line of data in the csv file will be of the following:
<status id>, <status date>, <content>

This scraper uses the snscraper library.
"""

import snscrape.modules.twitter as snt
import csv
from datetime import datetime
now = datetime.now()
current_date = now.date()
now = now.strftime('%Y-%m-%d')

#  user inputs
start_date = input('Input the start date YYYY/MM/DD')
max_tweets = int(input('How many tweets to scrape (int)'))

#   Convert start_date into a datetime object
start_date = datetime.strptime(start_date, "%Y/%m/%d")
start_date = start_date.date()

#  find tweets per day
day_delta = current_date - start_date
day_delta = day_delta.days
tweets_per_day = max_tweets // day_delta

# setting up the csv file and writer
# open csv file, make new one if file not found
csvFile = open('scraper-output/scrapes.csv', mode='a', newline='', encoding='utf8')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id', 'date', 'contents', ])

# scrape data
# currently the query and max_tweets must be changed manually in the script
# pass twitter queries into snt.TwitterSearchScraper() according to twitter rules
# in the future the keywords will be expanded and there will be inputs for dates and whatnot.
# and the scraper will only scrape a certain amount of tweets from each day, every day in a range

for i, tweet in enumerate(snt.TwitterSearchScraper('covid').get_items()):
    if i > max_tweets:
        break
    if i % 10 == 0:
        print(i)
    csvWriter.writerow([tweet.id, tweet.date, tweet.content])

csvFile.close()
