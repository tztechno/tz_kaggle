###########################################################

import random
import cv2
import matplotlib.pyplot as plt

selected_paths=random.sample(frame_paths,30)

# Create a 3x10 grid of subplots
fig, axs = plt.subplots(10, 3, figsize=(15, 35))
# Loop over the selected paths and display each image in a subplot
for i, path in enumerate(selected_paths):
    # Load the image and convert to RGB
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Compute the row and column indices of the subplot
    row, col = divmod(i, 3)
    # Display the image in the corresponding subplot
    axs[row, col].set_title(i)
    axs[row, col].imshow(img)
    axs[row, col].axis("off")
plt.show()

###########################################################

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

###########################################################
