import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load data (replace 'movie_ratings.csv' with your file path)
data = pd.read_csv("data.csv")

# Define app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(children=[
    html.H1("Movie Rating Exploration"),
    dcc.Dropdown(
        id="rating-dropdown",
        options=[{"label": str(rating), "value": rating} for rating in data["rating"].unique()],
        value=data["rating"].unique()[0]  # Pre-select first rating
    ),
    dcc.Graph(id="ratings-chart")
])

# Callback to update chart based on dropdown selection
@app.callback(
    Output("ratings-chart", "figure"),
    Input("rating-dropdown", "value")
)
def update_chart(selected_rating):
    filtered_data = data[data["rating"] == selected_rating]
    figure = px.bar(filtered_data, x="title", y="user_rating_score", title=f"Rating Distribution for {selected_rating} Movies")
    return figure

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
