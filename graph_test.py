"""Testing graphs and plot.ly"""

import plotly

import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="Covid things"
)
# fig.show()
fig.write_html('my_figure.html')
