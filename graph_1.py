""" CSC110 Final Project

This file is Copyright (c) 2021 Edward Han, Zekun Liu, Arvin Gingoyon
"""

import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import csv
from tweet import Tweet
import reader
import nltk

from analyzer import calc_word_emotions, calc_word_count, analyze_tweets


# helpers

# def load_data(filename: str) -> list[(str, dict)]:
#     """ Returns list of tuples in the format (date, score) for the given topic csv file"""
#
#     date_to_score_so_far = []
#
#     with open(filename) as file:
#         reader = csv.reader(file, delimiter=',')
#         next(reader)  # skip the header
#
#         for row in reader:
#             date_to_score_so_far.append((row[0], row[1]))  # (date, score)
#
#     return date_to_score_so_far
#
#
# topics_scores = []  # list[list[(str, dict)]]
#
#
# for topic_file in list_of_topics:
#     topics_scores.append(load_data(topic_file))
#
# avg_scores_so_far = []
#
# for i in range(len(list_of_topics)):
#     neg_so_far = 0
#     pos_so_far = 0
#     comp_so_far = 0
#     for str_dict in topics_scores[i]:
#         neg_so_far += str_dict[1]['negative']
#         pos_so_far += str_dict[1]['positive']
#         comp_so_far += str_dict[1]['compound']
#
#     avg_scores_so_far.append(neg_so_far)
#     avg_scores_so_far.append(pos_so_far)
#     avg_scores_so_far.append(comp_so_far)

# format input: list[(Tweet, score: dict, topic: {str})]

# list_of_topics = ['vaccine', 'masks', 'quarantine', 'conspiracy']

# Order of use:
# 1. use categorize and store it to a variable, lets say a
# 2. input a into average_scores and store output into a variable, lets say b
# 3. input b into function graph_1

def categorize(list_of_topics: list[str],
               tweet_data: list[tuple[Tweet, dict[str, float], set[str]]]) -> dict[str, list[dict]]:
    """ Returns a dictionary mapping each topic in list_of_topics to a list of
    all the dictionaries of scores for those topics

    """

    score_data_so_far = {}

    for t in list_of_topics:
        score_data_so_far[t] = []

    for tweet in tweet_data:
        for topic in tweet[2]:
            score_data_so_far[topic].append(tweet[1])

    return score_data_so_far


# above should give me {topic1: [{neg, pos, comp}, ...], topic2: [{neg, pos, comp}, ...]}

# helper for below
def average_list_dict(lst: list[dict[str, float]]) -> dict[str, float]:
    """ Returns average of each sentiment sign (pos, neg, comp) in list of score dictionaries"""
    dict_so_far = {}
    for dictionary in lst:
        for sentiment in dictionary:
            if sentiment not in dict_so_far:
                dict_so_far[sentiment] = 0
            dict_so_far[sentiment] += dictionary[sentiment]

    for key in dict_so_far:
        dict_so_far[key] = dict_so_far[key] / len(lst)

    return dict_so_far


def average_scores(topic_dict: dict[str, list[dict[str, float]]]) -> dict[str, dict[str, float]]:
    """ Return average negative, positive, compound for each topic"""
    new_topic_dict = {}
    for key in topic_dict:
        new_topic_dict[key] = average_list_dict(topic_dict[key])

    return new_topic_dict


# above gives me {topic1: {neg, pos, comp}, topic2: {neg, pos, comp}}

# set-up dataframe

def graph_1(list_of_topics: list[str], data: dict[str, dict[str, float]]) -> None:
    """ Creates graph"""

    topics = []
    scores = []
    for topic in data:
        for _ in range(3):
            topics.append(topic)
        for sent_score in data[topic]:
            if sent_score != 'neu':
                scores.append(abs(data[topic][sent_score]))

    df = pd.DataFrame({
        'Sentiment': ['Negative', 'Positive', 'Compound'] * len(data),
        'Topics': topics,
        'Sentiment Score': scores
    })

    # graph dataframe
    fig = px.bar(df, x='Topics', y='Sentiment Score', animation_frame='Sentiment',
                 animation_group='Topics', range_y=[0, 1], color='Sentiment', barmode='group')
    # fig.show()
    fig.write_html('my_figure.html')

# df = pd.DataFrame({
#     'Sentiment': ['Negative', 'Positive', 'Compound', 'Negative', 'Positive', 'Compound'],
#     'Topics': ['Covid', 'Covid', 'Covid', 'Vaccine', 'Vaccine', 'Vaccine'],
#     'Sentiment Score': [1, 2, 1, 3, 2, 1]
# })
