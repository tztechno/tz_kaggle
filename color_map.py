from matplotlib.colors import ListedColormap
import numpy as np
colors=np.load('/kaggle/input/color-palette/standard_color14.npy')
print(colors)
custom_cmap = ListedColormap(colors/255)
