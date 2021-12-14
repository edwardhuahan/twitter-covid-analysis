""" CSC110 Final Project

This file is Copyright (c) 2021 Edward Han, Zekun Liu, Arvin Gingoyon
"""

import plotly.express as px
import pandas as pd
from tweet import Tweet


# Order of use:
# 0. use reader function on csv, then use analyze_tweets function in analyzer on that output
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

def graph_1(data: dict[str, dict[str, float]]) -> None:
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
    fig1 = px.bar(df, x='Topics', y='Sentiment Score', animation_frame='Sentiment',
                  animation_group='Topics', range_y=[0, 1], color='Sentiment', barmode='group')

    fig1.update_layout(title_text='Topics to Average Sentiment Scores')
    fig1.show()
    # fig1.write_html('graph1.html')


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    python_ta.check_all(config={
        'extra-imports': ['plotly.express', 'pandas', 'tweet'],
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
