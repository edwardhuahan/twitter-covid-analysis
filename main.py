""" CSC110 Final Project

This file is Copyright (c) 2021 Edward Han, Zekun Liu, Arvin Gingoyon
"""

import analyzer
import graph_1
import graph_2
import graph_3
import reader

list_of_topics = ['vaccine', 'masks', 'quarantine', 'conspiracy', 'covid']
read_data = reader.read_tweet_data('test_data.csv')

# graph_1 processing
read_data_1 = analyzer.analyze_tweets(read_data)
a = graph_1.categorize(list_of_topics, read_data_1)
graph_1_data = graph_1.average_scores(a)

# graph_2 processing
scores = analyzer.analyze_sentiment(read_data)
clean = analyzer.clean_input(read_data)
roots = analyzer.split_into_stems(clean)
graph_2_data = analyzer.calc_word_emotions(scores, roots)

# graph_3 processing
read_data_3 = analyzer.analyze_tweets(read_data)
sorted_tweets = graph_3.sort_tweets_by_date(read_data_3)
graph_3_data = graph_3.average_scores(sorted_tweets)


def run_graphs() -> None:
    """ Creates all 3 graphs"""
    graph_1.graph_1(graph_1_data)
    graph_2.graph_2(graph_2_data)
    graph_3.graph_3(graph_3_data)
