"""Testing graphs and plot.ly"""

import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import csv

# fig = go.Figure(
#     data=[go.Bar(y=[2, 1, 3])],
#     layout_title_text="Covid things"
# )
# fig.show()
# # fig.write_html('my_figure.html')

# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Contestant": ["Alex", "Alex", "Alex", "Jordan", "Jordan", "Jordan"],
#     "Number Eaten": [2, 1, 3, 1, 3, 2]
# })
#
# fig = px.bar(df, x='Fruit', y='Number Eaten', animation_frame='Fruit', animation_group='Contestant',
#              color='Contestant', barmode='group')


# def format_graph_data(data: list[(Tweet, score, topic)]) -> Dataframe:
#     """ Formats tweet data post-processing and returns a pandas dataframe for graph"""
#     dict_data = {'Sentiment': [], 'Topics': [], 'Score': []}
#     for data in range(len(data)):
#         if data[2] not in
#             dict_data[''] = dict_data['Sentiment'] + []
#
#     graph_data = pd.DataFrame(dict_data)
#
#     return graph_data

list_of_topics = []


# helpers

def load_data(filename: str) -> list[(str, dict)]:
    """ Returns list of tuples in the format (date, score) for the given topic csv file"""

    date_to_score_so_far = []

    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)  # skip the header

        for row in reader:
            date_to_score_so_far.append((row[0], row[1]))  # (date, score)

    return date_to_score_so_far


topics_scores = []  # list[list[(str, dict)]]


for topic_file in list_of_topics:
    topics_scores.append(load_data(topic_file))

avg_scores_so_far = []

for i in range(len(list_of_topics)):
    neg_so_far = 0
    pos_so_far = 0
    comp_so_far = 0
    for str_dict in topics_scores[i]:
        neg_so_far += str_dict[1]['negative']
        pos_so_far += str_dict[1]['positive']
        comp_so_far += str_dict[1]['compound']

    avg_scores_so_far.append(neg_so_far)
    avg_scores_so_far.append(pos_so_far)
    avg_scores_so_far.append(comp_so_far)


# set-up dataframe

topics = []
for topic in list_of_topics:
    for _ in range(3):
        topics.append(topic)

df = pd.DataFrame({
    'Sentiment': ['Negative', 'Positive', 'Compound'] * len(list_of_topics),
    'Topics': topics,
    'Sentiment Score': avg_scores_so_far
})

# df = pd.DataFrame({
#     'Sentiment': ['Negative', 'Positive', 'Compound', 'Negative', 'Positive', 'Compound'],
#     'Topics': ['Covid', 'Covid', 'Covid', 'Vaccine', 'Vaccine', 'Vaccine'],
#     'Sentiment Score': [1, 2, 1, 3, 2, 1]
# })

# graph dataframe
fig = px.bar(df, x='Topics', y='Sentiment Score', animation_frame='Sentiment',
             animation_group='Topics', range_y=[0, 5], color='Sentiment', barmode='group')
# fig.show()
fig.write_html('my_figure.html')
