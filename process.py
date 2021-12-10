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
    date: datetime.datetime
    content: str

    def __init__(self, tweet_id: int, date: datetime.datetime, content: str):
        self.tweet_id = tweet_id
        self.date = date
        self.content = content


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

    calendar = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
        'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
        'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }

    split_data = raw_time.split(' ')
    split_time = [int(value) for value in split_data[3].split(':')]
    parsed_data = datetime.datetime(day=int(split_data[2]), month=calendar[split_data[1]],
                                    year=int(split_data[5]), hour=split_time[0],
                                    minute=split_time[1], second=split_time[2])

    return parsed_data
