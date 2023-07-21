import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

colors = px.colors.cyclical.Phase


def create_bar_graph(x_values, y_values):
  sorted_data = sorted(zip(x_values, y_values),
                       key=lambda x: x[1],
                       reverse=True)
  x_categories, y_values = zip(*sorted_data)
  fig = go.Figure(
    data=[go.Bar(x=x_categories, y=y_values, marker_color=colors)])
  fig.update_layout(title='Sentiment Analysis Results',
                    xaxis_title='Sentiment',
                    yaxis_title='Certainty Score',
                    paper_bgcolor='#FFFFFF',
                    plot_bgcolor='#FFFFFF',
                    title_font_size=45,
                    font_family="Roboto",
                    xaxis=dict(tickmode='linear'))
  fig = fig.to_json()
  return fig
