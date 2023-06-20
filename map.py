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
