import plotly.express as px
import pandas as pd
import plotly.io as pio

# Load the data (assuming 'AQI and Lat Long of Countries.csv' is a large file with many rows)
data = pd.read_csv('AQI and Lat Long of Countries.csv')

# Check if the data loads correctly and inspect the first few rows
print(data.head())

# Plot the data using a scatter plot on the map
# 'color' is used to represent the heatmap value (AQI Value)
# 'size' will adjust the marker size based on the AQI value
fig = px.scatter_mapbox(data, lat='lat', lon='lng',
                        color='AQI Value',
                        size='AQI Value',
                        color_continuous_scale='Viridis',  # Color scale for the points
                        size_max=15,  # Maximum size of the points
                        zoom=1,  # Adjust zoom for a global view
                        mapbox_style="carto-positron")  # You can change the style as you prefer

# Update layout to make the map bigger
fig.update_layout(
    mapbox_accesstoken='your_mapbox_access_token',  # If needed, add Mapbox token here
    margin={"r":0,"t":0,"l":0,"b":0},  # Removing margins for a full-screen map
    height=600  # Set the map height
)

# Save the map as an HTML file
pio.write_html(fig, 'map.html')

# Optional: Display the map in the browser after saving (uncomment the following line if needed)
# fig.show()
