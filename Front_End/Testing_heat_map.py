import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

# Load your dataset
data = pd.read_csv('AQI and Lat Long of Countries.csv')

# Initialize a blank figure
fig = go.Figure()

# Add NO2 AQI trace (visible by default)
fig.add_trace(go.Scattermapbox(
    lat=data['lat'],
    lon=data['lng'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=data['NO2 AQI Value'],
        color=data['NO2 AQI Value'],
        colorscale='Viridis',
        sizemode='area',
        sizeref=2.*max(data['NO2 AQI Value'])/(15.**2),
        colorbar=dict(title="NO2 AQI"),
    ),
    name='NO2 AQI',
    visible=True  # Visible by default
))

# Add CO AQI trace (hidden initially)
fig.add_trace(go.Scattermapbox(
    lat=data['lat'],
    lon=data['lng'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=data['CO AQI Value'],
        color=data['CO AQI Value'],
        colorscale='Cividis',
        sizemode='area',
        sizeref=2.*max(data['CO AQI Value'])/(15.**2),
        colorbar=dict(title="CO AQI"),
    ),
    name='CO AQI',
    visible=False  # Hidden by default
))

# Add Ozone AQI trace (hidden initially)
fig.add_trace(go.Scattermapbox(
    lat=data['lat'],
    lon=data['lng'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=data['Ozone AQI Value'],
        color=data['Ozone AQI Value'],
        colorscale='Plasma',
        sizemode='area',
        sizeref=2.*max(data['Ozone AQI Value'])/(15.**2),
        colorbar=dict(title="Ozone AQI"),
    ),
    name='Ozone AQI',
    visible=False  # Hidden by default
))

# Set up the layout, including the map style
fig.update_layout(
    mapbox=dict(
        style="carto-positron",
        zoom=1,
        center=dict(lat=20, lon=0),  # Centered globally
    ),
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    height=600,

    # Add dropdown menu buttons to switch between datasets
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [{"visible": [True, False, False]}],  # Show NO2 AQI only
                    "label": "NO2 AQI",
                    "method": "update"
                },
                {
                    "args": [{"visible": [False, True, False]}],  # Show CO AQI only
                    "label": "CO AQI",
                    "method": "update"
                },
                {
                    "args": [{"visible": [False, False, True]}],  # Show Ozone AQI only
                    "label": "Ozone AQI",
                    "method": "update"
                }
            ],
            "direction": "down",
            "showactive": True,
        }
    ]
)

# Save the map as an HTML file
pio.write_html(fig, 'map_with_buttons.html')

# Optional: Display the map in the browser
fig.show()
