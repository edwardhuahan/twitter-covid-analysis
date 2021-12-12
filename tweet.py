""" CSC110 Final Project

This file is Copyright (c) 2021 Edward Han, Zekun Liu, Arvin Gingoyon
"""
import datetime


class Tweet:
    """ Tweet dataclass

    Instance Attributes:
      - tweet_id: the integer id of the tweet
      - date: the date that the tweet was published as a datetime.datetime
      - content: the contents of the string in string format

    Representation Invariants:
      - self.tweet_id >= 0
    """
    tweet_id: int
    date: datetime.datetime
    content: str

    def __init__(self, tweet_id: int, date: datetime.datetime, content: str):
        self.tweet_id = tweet_id
        self.date = date
        self.content = content
