import numpy as np
import matplotlib.pyplot as plt

# データポイントの座標を生成
x = np.random.randn(1000)
y = np.random.randn(1000)

# ヒストグラムを計算
heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)

# プロット領域を作成
fig, ax = plt.subplots()

# ヒートマップを描画
im = ax.imshow(heatmap.T, cmap='hot', origin='lower', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])

# カラーバーを追加
cbar = fig.colorbar(im)

# ラベルやタイトルなどのカスタマイズ
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Heat Map')

# グリッドを表示
ax.grid(True)

# プロットを表示
plt.show()
