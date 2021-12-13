"""
DEC 09 2021

CSC Final Project 2021

This script is used to scrape tweets from twitter for use in my csc110 final project
The scraper accepts a range of dates and outputs the tweets into a csv file.
Each line of data in the csv file will be of the following:
<status id>, <status date>, <content>
The following is the csv header:
id,date,contents

!!!!!!!!!!!!!!!!!!!!!!!!!!!1
TWITTER API SUCKS AND EVERYTIME YOU START A NEW SCRAPE REQUEST THERE IS A CHANCE IT'S GOING TO
DECLINE GIVING SNSCRAPER A GUEST TOKEN
WHICH MEANS THAT EVERY TIME IT SEARCHES FOR A NEW DAY THERE'S A CHANCE IT JUST BRICKS BECAUSE
TWITTER WANTS IT TO
THERE'S NO WAY AROUND THIS EXCEPT REQUEST MORE TWEETS EACH DAY TO MINIMIZE THE RISK

This file is Copyright (c) 2021 Edward Han, Zekun Liu (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧, Arvin Gingoyon
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
tweets_per_day = max_tweets // (day_delta + 1)

# setting up the csv file and writer
# open csv file, make new one if file not found
csvFile = open('scraper-output/scrapes.csv', mode='a', newline='', encoding='utf8')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id', 'date', 'contents', ])

# scrape data
while start_date <= current_date:

    dt = start_date.strftime('%Y-%m-%d')
    dtn = start_date + timedelta(days=1)
    dtn = dtn.strftime('%Y-%m-%d')

    search_term = f'covid OR coronavirus OR covid19 OR corona lang:en since:{dt} until:{dtn}'

    for i, tweet in enumerate(snt.TwitterSearchScraper(search_term).get_items()):
        if i > tweets_per_day:
            break
        print(f'Found tweet number {i} for date {dt}')
        csvWriter.writerow([tweet.id, tweet.date, tweet.content])
    start_date += timedelta(days=1)

csvFile.close()
