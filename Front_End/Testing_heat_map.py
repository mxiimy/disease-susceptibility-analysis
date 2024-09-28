import plotly.express as px
import pandas as pd
import plotly.io as pio
import os

data = pd.read_csv('AQI and Lat Long of Countries.csv')  

fig = px.scatter_mapbox(data, lat='lat', lon='lng',
                        color='AQI Value',
                        size='AQI Value',
                        color_continuous_scale='Viridis',
                        size_max=15,
                        zoom=1,
                        mapbox_style="carto-positron")


pio.write_html(fig, 'map.html', auto_open=True)
