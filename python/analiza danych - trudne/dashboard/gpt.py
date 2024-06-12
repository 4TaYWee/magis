import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import time

# Record compilation time
compilation_start_time = time.time()

# Sample data
data = {
    'Country': ['USA', 'Canada', 'Germany', 'UK', 'France'],
    'Population': [327, 38, 83, 66, 67],  # in millions
    'GDP': [21.43, 1.84, 4.42, 2.83, 2.78]  # in trillions
}

df = pd.DataFrame(data)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Interactive Dashboard"),
    html.Label("Select a metric to visualize:"),
    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Population', 'value': 'Population'},
            {'label': 'GDP', 'value': 'GDP'}
        ],
        value='Population'
    ),
    dcc.Graph(id='my-graph')
])

# Define callback to update the graph based on dropdown selection
@app.callback(
    Output('my-graph', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_graph(selected_metric):
    fig = px.bar(df, x='Country', y=selected_metric, title=f'{selected_metric} by Country')
    return fig

# Record compilation time
compilation_end_time = time.time()

# Print compilation time
print(f"Compilation time: {compilation_end_time - compilation_start_time} seconds")

# Run the app
if __name__ == '__main__':
    # Record execution time
    execution_start_time = time.time()
    
    # Run the app
    app.run_server(debug=True)
    
    # Record execution time
    execution_end_time = time.time()
    
    # Print execution time
    print(f"Execution time: {execution_end_time - execution_start_time} seconds")
