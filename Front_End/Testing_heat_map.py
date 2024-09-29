import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

data = pd.read_csv('AQI and Lat Long of Countries.csv')
sample_data = pd.read_csv('AQdata.csv')

fig = go.Figure()

# Add Actual Data (visible by default)
fig.add_trace(go.Scattermapbox(
    lat=sample_data['lat'],
    lon=sample_data['lng'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=sample_data['PM2.5'],
        color=sample_data['PM2.5'],
        colorscale='Viridis',
        sizemode='area',
        sizeref=2.*max(sample_data['PM2.5'])/(15.**2),
        colorbar=dict(title="PM2.5"),
    ),
    visible=True,
    hovertemplate='<b>PM2.5</b> <br>'+
                  '<b>Coordinates:</b> (%{lon:.2f}, %{lat:.2f})<br>' +
                  '<b>Value:</b> %{marker.color:.2f}<br>' +
                  '<extra></extra>',
))

# Add NO2 AQI trace (hidden initially)
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
    visible=False,
    hovertemplate='<b>NO2 AQI</b> <br>'+
                  '<b>Coordinates:</b> (%{lon:.2f}, %{lat:.2f})<br>' +
                  '<b>Value:</b> %{marker.color:.2f}<br>' +
                  '<b>Country:</b> %{customdata}<br>'+
                  '<extra></extra>',
    customdata=data['Country']
))

# Repeat for CO AQI trace
fig.add_trace(go.Scattermapbox(
    lat=data['lat'],
    lon=data['lng'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=data['CO AQI Value'],
        color=data['CO AQI Value'],
        colorscale='Magma',
        sizemode='area',
        sizeref=2.*max(data['CO AQI Value'])/(15.**2),
        colorbar=dict(title="CO AQI"),
    ),
    visible=False,
    hovertemplate='<b>CO AQI</b> <br>' +
                  '<b>Coordinates:</b> (%{lon:.2f}, %{lat:.2f})<br>' +
                  '<b>Value:</b> %{marker.color:.2f}<br>' +
                  '<b>Country:</b> %{customdata}<br>' +
                  '<extra></extra>',
    customdata=data['Country']
))

# Ozone AQI trace (hidden initially)
fig.add_trace(go.Scattermapbox(
    lat=data['lat'],
    lon=data['lng'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=data['Ozone AQI Value'],
        color=data['Ozone AQI Value'],
        colorscale='Aggrnyl',
        sizemode='area',
        sizeref=2.*max(data['Ozone AQI Value'])/(15.**2),
        colorbar=dict(title="Ozone AQI"),
    ),
    visible=False,
    hovertemplate='<b>Ozone AQI</b> <br>' +
                  '<b>Coordinates:</b> (%{lon:.2f}, %{lat:.2f})<br>' +
                  '<b>Value:</b> %{marker.color:.2f}<br>' +
                  '<b>Country:</b> %{customdata}<br>'+
                  '<extra></extra>',
    customdata=data['Country']
))

fig.update_layout(
    mapbox=dict(
        style="carto-positron",
        zoom=1,
        center=dict(lat=20, lon=0),  # Centered globally
    ),
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    height=600,
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [{"visible": [True, False, False, False]}],
                    "label": "Our data",
                    "method": "update"
                },
                {
                    "args": [{"visible": [False, True, False, False]}],
                    "label": "NO2 AQI",
                    "method": "update"
                },
                {
                    "args": [{"visible": [False, False, True, False]}],
                    "label": "CO AQI",
                    "method": "update"
                },
                {
                    "args": [{"visible": [False, False, False, True]}],
                    "label": "Ozone AQI",
                    "method": "update"
                }
            ],
            "direction": "down",
            "showactive": True,
        }
    ]
)

pio.write_html(fig, '../map_with_buttons.html')
fig.show()
