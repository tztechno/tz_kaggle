import numpy as np 
import pandas as pd 
import geopandas as gpd
import plotly.express as px
import matplotlib.pyplot as plt
from shapely.wkt import loads
from shapely.geometry import Point
from branca.colormap import linear


dataj = gpd.read_file('/kaggle/input/earthquake-in-japan/gadm41_JPN_1.json')
dataj['color']=dataj.index.tolist()
print(len(dataj))
print(sorted(dataj['NAME_1'].tolist()))

colormap = linear.YlOrRd_05.scale(0,46)

fig, ax = plt.subplots(figsize=(20,20))
for i in range(len(dataj)):
    di = dataj.loc[i,'geometry']
    dc = dataj.loc[i,'color']
    color=colormap(dc)  
    gdfi = gpd.GeoDataFrame(geometry=[di])
    gdfi.plot(ax=ax,color=color,alpha=1)

plt.title('json')
plt.show()
