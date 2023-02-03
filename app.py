import folium
import pandas as pd
import streamlit as st
from folium.plugins import HeatMap

st.title('Mapping Potholes')

from streamlit_folium import st_folium
df_acc = pd.read_csv('test-cv.csv', dtype=object)

# center on Liberty Bell, add marker
m = folium.Map(location=[51.521709, -0.212653], zoom_start=13)

# Ensure you're handing it floats
df_acc['Latitude'] = df_acc['Latitude'].astype(float)
df_acc['Longitude'] = df_acc['Longitude'].astype(float)

heat_df = df_acc[['Latitude', 'Longitude']]
heat_df = heat_df.dropna(axis=0, subset=['Latitude','Longitude'])
heat_data = [[row['Latitude'],row['Longitude']] for index, row in heat_df.iterrows()]
HeatMap(heat_data).add_to(m)


# folium.Marker(
#     [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
# ).add_to(m)

# call to render Folium map in Streamlit



st_data = st_folium(m, height=400, width=1920)