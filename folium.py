import folium
from folium import plugins

eq_map = folium.Map(location=[41.9,-87.7],tiles='Stamen Terrain',zoom_start=10.0,min_zoom=2.0)
eq_map.add_child(plugins.HeatMap(data3))
eq_map
