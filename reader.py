""" CSC110 Final Project

Edward Han, Zekun Liu, Arvin Gingoyon
"""
import csv
import datetime
from tweet import Tweet


def read_tweet_data(filename: str) -> list[Tweet]:
    """ Read csv file data
    """

    inputs_so_far = []

    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        # Skip the header because it is not useful
        next(reader)

        for row in reader:
            id = int(row[0])
            raw_date = row[1]
            content = row[2]

            tweet = Tweet(id, parse_time(raw_date), content)
            inputs_so_far.append(tweet)

    return inputs_so_far


def parse_time(raw_time: str) -> datetime.datetime:
    """
        Take a raw unparsed date and time string as input and return a
        datetime.datetime object
    """

    date_and_time = raw_time.split(' ')
    split_date = [int(value) for value in date_and_time[0].split('-')]
    split_time = [value for value in date_and_time[1].split(':')]
    parsed_data = datetime.datetime(day=split_date[2], month=split_date[1],
                                    year=split_date[0], hour=int(split_time[0]),
                                    minute=int(split_time[1]))

    return parsed_data
