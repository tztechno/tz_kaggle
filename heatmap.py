import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)
y = np.random.randn(1000)

heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)

fig, ax = plt.subplots()

im = ax.imshow(heatmap.T, cmap='hot', origin='lower', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])

#'hot': 赤から黄色までのホットなカラーマップです。高い値がより明るい色で表示されます。
#'cool': 青からシアンまでのクールなカラーマップです。低い値がより明るい色で表示されます。
#'viridis': カラーマップの感じに基づいた色のマッピングです。低い値から高い値に徐々に変化し、黄緑から深い青までの範囲をカバーします。
#'magma': 黒から赤紫までのマグマのようなカラーマップです。低い値から高い値に徐々に変化し、暗い色から明るい色までを含みます。
#'inferno': 黒から黄色までのインフェルノのようなカラーマップです。低い値から高い値に徐々に変化し、暗い色から明るい色までを含みます。

cbar = fig.colorbar(im)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Heat Map')
ax.grid(True)
plt.show()
