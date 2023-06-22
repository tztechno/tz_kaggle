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

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# 地図の範囲を設定します
map = Basemap(llcrnrlon=120, llcrnrlat=20, urcrnrlon=160, urcrnrlat=50, resolution='l')

# 地図の背景を描画します
map.drawmapboundary(fill_color='lightblue')
map.fillcontinents(color='white', lake_color='lightblue')

# 緯度経度に基づいて都市の位置をプロットします
cities = {
    'Tokyo': (139.6917, 35.6895),
    'Osaka': (135.5022, 34.6937),
    'Sapporo': (141.3545, 43.0621)
}

for city, (lon, lat) in cities.items():
    x, y = map(lon, lat)
    map.plot(x, y, 'ro', markersize=5)
    plt.text(x, y, city, fontsize=8, ha='left', va='center')

# プロットを表示します
plt.show()

###########################################################

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# 地図の範囲を設定します
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([120, 160, 20, 50])

# 地図の背景を描画します
ax.stock_img()

# 緯度経度に基づいて都市の位置をプロットします
cities = {
    'Tokyo': (139.6917, 35.6895),
    'Osaka': (135.5022, 34.6937),
    'Sapporo': (141.3545, 43.0621)
}

for city, (lon, lat) in cities.items():
    ax.plot(lon, lat, 'ro', markersize=5, transform=ccrs.PlateCarree())
    ax.text(lon, lat, city, fontsize=8, ha='left', va='center', transform=ccrs.PlateCarree())

# プロットを表示します
plt.show()

###########################################################
