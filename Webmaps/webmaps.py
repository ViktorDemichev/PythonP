import folium
import pandas   

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location = [50, -50])

fg = folium.FeatureGroup(name = "MyGroup")