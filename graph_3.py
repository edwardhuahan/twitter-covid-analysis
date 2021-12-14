""" CSC110 Final Project

This file is Copyright (c) 2021 Edward Han, Zekun Liu, Arvin Gingoyon
"""

import plotly.express as px
import pandas as pd
from tweet import Tweet
from graph_1 import average_list_dict


def sort_tweets_by_date(
        tweets: list[tuple[Tweet, dict[str, float], set[str]]]) -> dict[str, list[dict]]:
    """ Returns dictionary mapping days of tweets to a list of the scores of all the tweets
    belonging to that day"""

    days_so_far = {}
    for tweet in tweets:
        month = str(tweet[0].date.month)
        day = str(tweet[0].date.day)
        year = str(tweet[0].date.year)
        month_day_year = month + '/' + day + '/' + year
        if month_day_year not in days_so_far:
            days_so_far[month_day_year] = []
        days_so_far[month_day_year].append(tweet[1])

    return days_so_far


def average_scores(
        tweet_scores: dict[str, list[dict[str, float]]]) -> dict[str, dict[str, float]]:
    """ Maps dates to the average of its respective compound scores"""

    compound_tweet_so_far = {}
    for date in tweet_scores:
        compound_tweet_so_far[date] = average_list_dict(tweet_scores[date])

    return compound_tweet_so_far


def graph_3(tweet_data: dict[str, dict[str, float]]) -> None:
    """ Creates line graph displaying compound scores over dates"""

    dates = []
    comp_scores = []

    for date in tweet_data:
        dates.append(date)
        comp_scores.append(tweet_data[date]['compound'])

    df = pd.DataFrame({
        'Dates': dates,
        'Average Compound Score': comp_scores
    })

    fig3 = px.line(df, x='Dates', y='Average Compound Score')

    fig3.update_layout(title_text='Compound Sentiment Score over Time')
    fig3.show()
    # fig3.write_html('graph3.html')


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    python_ta.check_all(config={
        'extra-imports': ['plotly.express', 'pandas', 'tweet', 'graph_1'],
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
