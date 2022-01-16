import folium
import pandas

data = pandas.read_csv("D:\Python\supermarkets\Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000 :
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,--99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Group")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el), icon=folium.Icon(color=color_producer(el)), color='grey', fill_opacity=0.7, fill=True))
map.add_child(fg)
map.save("D:\MapCircle.html")
