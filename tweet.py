""" CSC110 Final Project

Edward Han, Zekun Liu, Arvin Gingoyon
"""
import datetime


class Tweet:
    """
        Tweet dataclass
    """
    tweet_id: int
    date: datetime.datetime
    content: str

    def __init__(self, tweet_id: int, date: datetime.datetime, content: str):
        self.tweet_id = tweet_id
        self.date = date
        self.content = content
