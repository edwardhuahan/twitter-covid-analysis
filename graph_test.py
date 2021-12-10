"""Testing graphs and plot.ly"""

import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

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

# Ignore this, this doesn't work
df = pd.DataFrame({
    'Months': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
               'September', 'October', 'November', 'December'],
    "Topics": ["Apples", "Oranges", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'w', 'y'],
    "Number Eaten": [10, 50, 20, 30, 100, 17, 10, 50, 20, 30, 100, 17]
})

fig = px.bar(df, x='Months', y='Number Eaten', animation_frame='Months', animation_group='Topics',
             color='Topics', range_y=[25, 90], barmode='group')
fig.show()
