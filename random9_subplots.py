
import random
import matplotlib.pyplot as plt
import numpy as np

# ランダムに9個のデータを選ぶ
indices = np.random.choice(len(dataX), size=9, replace=False)

# 3x3のグリッドに表示する
fig, axs = plt.subplots(3, 3, figsize=(8, 8))
for i, ax in enumerate(axs.flatten()):
    ax.imshow(dataX[indices[i]])
    ax.set_title(str(dataY[indices[i]]))
    ax.axis('off')
plt.tight_layout()
plt.show()
