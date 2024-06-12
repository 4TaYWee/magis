import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px  # Import plotly.express

# Sample data (replace with your data source)
data = pd.Series({'2020': 25, '2021': 32, '2022': 40, '2023': 51}, name='Values')
years = data.index.tolist()

# Define the app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in years],
        value=years[0]  # Default selected year
    ),
    dcc.Graph(id='line-chart')
])

# Callback to update chart based on dropdown selection
@app.callback(
    Output(component_id='line-chart', component_property='figure'),
    Input(component_id='year-dropdown', component_property='value')
)
def update_chart(selected_year):
    # Filter data based on selected year
    filtered_data = data[selected_year]

    # Create line chart
    fig = px.line(x=filtered_data.index, y=filtered_data.values)
    fig.update_layout(title=f'Value Trend ({selected_year})')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
