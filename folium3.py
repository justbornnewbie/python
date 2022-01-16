import folium
import pandas

data = pandas.read_csv("D:\Python\supermarkets\Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[19,72.8], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Group")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el), icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("D:\Map.html")
