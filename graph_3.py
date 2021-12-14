""" CSC110 Final Project

This file is Copyright (c) 2021 Edward Han, Zekun Liu, Arvin Gingoyon
"""

import datetime
import reader
import plotly.express as px
import pandas as pd
from tweet import Tweet
import analyzer
from graph_1 import average_list_dict


# recall format of tweets: list[tuple[Tweet, dict[str, float], set[str]]]


def sort_tweets_by_date(
        tweets: list[tuple[Tweet, dict[str, float], set[str]]]) -> dict[str, list[dict]]:
    """ Returns dictionary mapping days of tweets to a list of the scores of all the tweets
    belonging to that day"""
    days_so_far = {}
    for tweet in tweets:
        month_day_year = str(tweet[0].date.month) + '/' + \
                         str(tweet[0].date.day) + '/' + str(tweet[0].date.year)
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
    """ Creates graph"""
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
    fig3.write_html('graph3.html')
