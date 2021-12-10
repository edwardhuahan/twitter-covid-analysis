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

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Contestant": ["Alex", "Alex", "Alex", "Jordan", "Jordan", "Jordan"],
    "Number Eaten": [2, 1, 3, 1, 3, 2],
})

# fig = px.bar(df, x="Fruit", y="Number Eaten", color="Contestant", barmode="group")
fig = px.line_3d(df, x="Fruit", y="Number Eaten", color="Contestant")
fig.show()
