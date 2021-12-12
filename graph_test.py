"""Testing graphs and plot.ly"""

import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import tweet
import analyzer

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

df = pd.DataFrame({
    'Sentiment_labels': ['Negative', 'Positive', 'Compound', 'Negative', 'Positive', 'Compound'],
    'Topics': ['Covid', 'Covid', 'Covid', 'Vaccine', 'Vaccine', 'Vaccine'],
    'Sentiment_score': [1, 2, 1, 3, 2, 1]
})

fig = px.bar(df, x='Topics', y='Sentiment_score', animation_frame='Sentiment_labels',
             animation_group='Topics', range_y=[0, 5], barmode='group')
fig.show()
fig.write_html('my_figure.html')
