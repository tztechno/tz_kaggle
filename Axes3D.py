
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = train['x1']
y = train['x2']
z = train['x3']
label=train['label']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=label, cmap='viridis')  # 'viridis'カラーマップを使用

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# カラーバーを追加してラベルを表示
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Label')

plt.show()

-----------------------------------------

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
z = [0, 0, 0, 0, 0]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

