"""
DEC 09 2021

CSC Final Project 2021

This script is used to scrape tweets from twitter for use in my csc110 final project
The scraper accepts a range of dates and outputs the tweets into a csv file.
Each line of data in the csv file will be of the following:
<status id>, <status date>, <content>
The following is the csv header:
id,date,contents

EVERYTIME YOU START A NEW SCRAPE REQUEST FOR TWITTER API THERE IS A CHANCE IT'S GOING TO
DECLINE GIVING SNSCRAPER A GUEST TOKEN
WHICH MEANS THAT EVERY TIME IT SEARCHES FOR A NEW DAY THERE'S A CHANCE IT BREAKS
THERE'S NO WAY AROUND THIS EXCEPT REQUEST MORE TWEETS EACH DAY TO MINIMIZE THE RISK

This file is Copyright (c) 2021 Edward Han, Zekun Liu (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧, Arvin Gingoyon
"""

import csv
from datetime import datetime, timedelta
import snscrape.modules.twitter as snt


def scrape(start_date: str, max_tweets: int) -> None:
    """ Takes a start date and tweet limit and exports tweets from date range
    to export into a CSV file containing tweet id, tweet content and tweet date.

    :param start_date: Str, A date in the format YYYY/MM/DD
    :param max_tweets: Int, The number of total tweets you want
    :return: None, creates a csv file with the scraped tweets
    """
    now = datetime.now()
    current_date = now.date()
    # now = now.strftime('%Y-%m-%d')

    #  user inputs
    #  has been moved to the parameters

    #   Convert start_date into a datetime object
    start_date = datetime.strptime(start_date, "%Y/%m/%d")
    start_date = start_date.date()

    #  find tweets per day
    day_delta = current_date - start_date
    day_delta = day_delta.days
    tweets_per_day = max_tweets // (day_delta + 1)

    # setting up the csv file and writer
    # open csv file, make new one if file not found
    with open('scraper-output/scrapes.csv', mode='a', newline='', encoding='utf8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['id', 'date', 'contents', ])

        # scrape data
        while start_date <= current_date:

            dt = start_date.strftime('%Y-%m-%d')
            dtn = next_day(start_date)
            dtn = dtn.strftime('%Y-%m-%d')

            search_term = f'covid OR coronavirus OR covid19' \
                          f' OR corona lang:en since:{dt} until:{dtn}'

            for i, tweet in enumerate(snt.TwitterSearchScraper(search_term).get_items()):
                if i > tweets_per_day:
                    break
                print(f'Found tweet number {i} for date {dt}')
                csv_writer.writerow([tweet.id, tweet.date, tweet.content])
            start_date += timedelta(days=1)

        csv_file.close()


def next_day(original_date: datetime.date) -> datetime.date:
    """ Takes a datetime and returns the day after the date specified
    in the object. This function is needed because simply adding
    datetime.timedelta(days=1) to datetime.datetime.now() is not testable

    >>> example = datetime(2021, 12, 1)
    >>> next_day(example)
    datetime.datetime(2021, 12, 2, 0, 0)

    """
    return original_date + timedelta(days=1)


if __name__ == "__main__":
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    python_ta.check_all(config={
        'extra-imports': ['snscrape.modules.twitter', 'csv', 'datetime'],
        'allowed-io': ['scrape'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    scrape('2021/12/09', 1000)  # Default values
