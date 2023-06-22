###########################################################
import seaborn as sns
import geopandas as gpd

sns.set_style('whitegrid')
sns.scatterplot(data = airports_data, x='lon', y='lat', hue='alt')
plt.title('The highest and lowesst airports')

# initialize an axis + adding default Austrlia map
fig, ax = plt.subplots(figsize=(8,6))
countries = gpd.read_file(  
     gpd.datasets.get_path("naturalearth_lowres"))
countries[countries["name"] == "Australia"].plot(color="lightgrey",ax=ax)
#building scatter graph
airports_data[airports_data['country']=='Australia'].plot(x="lon", y="lat", kind="scatter", colormap="YlOrRd", ax=ax)
plt.title('All the airports in Australia')
plt.show()

###########################################################
import folium
from folium import plugins
import seaborn as sns
import matplotlib.pyplot as plt

eq_map = folium.Map(location=[41.9,-87.7],tiles='Stamen Terrain',zoom_start=10.0,min_zoom=2.0)
eq_map.add_child(plugins.HeatMap(data3))
eq_map

###########################################################
