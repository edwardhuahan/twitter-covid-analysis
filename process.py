""" CSC110 Final Project

Edward Han, Zekun Liu, Arvin Gingoyon
"""
import csv
import datetime


class Tweet:
    """
        Tweet dataclass
    """
    tweet_id: int
    date: str
    content: str

    def __init__(self, tweet_id: int, date: str):
        self.tweet_id = tweet_id
        self.date = date


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

            tweet = Tweet(id, raw_date)
            inputs_so_far.append(tweet)

    return inputs_so_far
