import folium
import pandas

def pro_color(elevation):
  if elevation <= 1000:
    return "darkred"
  elif elevation <= 2000:
    return "orange"
  else:
    return "red"
map = folium.Map(location = [38.58, -99.09], zoom_start = 5, tiles = "Stamen Terrain")

vol_cd = pandas.read_csv("Volcanoes.txt")
lat = list(vol_cd["LAT"])
lon = list(vol_cd["LON"])
ele = list(vol_cd["ELEV"])


fg = folium.FeatureGroup(name = "My Map")
for lt,ln,el in zip(lat,lon,ele):
  fg.add_child(folium.CircleMarker(location = [lt,ln], radius = 6, popup = folium.Popup(str(el) + " m", parst_html = True), fill_color = pro_color(el), color = pro_color(el)))
#fg.add_child(folium.GeoJson(data = ( open('world.json').read(), encoding="utf-8")))

map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("Map1.html")