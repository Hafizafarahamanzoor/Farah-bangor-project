# Import necessary libraries
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
# Sample data
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Population': [8398748, 3990456, 2705994, 2325502, 1680992],
    'Area': [468.9, 1213.9, 227.3, 669.2, 1340.6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("City Statistics Dashboard"),
    dcc.Graph(
        id='population-bar-chart',
        figure=px.bar(df, x='City', y='Population', title='Population by City')
    ),
    dcc.Graph(
        id='area-pie-chart',
        figure=px.pie(df, values='Area', names='City', title='Area Distribution by City')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
