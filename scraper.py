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
from datetime import datetime, timedelta
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
# pass twitter queries into snt.TwitterSearchScraper() according to twitter rules
while start_date <= current_date:
    # print(f'Current Date:{start_date}')
    dt = start_date.strftime('%Y-%m-%d')
    search_term = f'covid OR coronavirus OR covid19 OR corona lang:en since:{dt} until:{dt}'
    print(f'search term:{search_term}')
    for i, tweet in enumerate(snt.TwitterSearchScraper(search_term).get_items()):
        if i > tweets_per_day:
            break
        if i % 10 == 0:
            print(i)
        csvWriter.writerow([tweet.id, tweet.date, tweet.content])
    start_date += timedelta(days=1)

csvFile.close()
