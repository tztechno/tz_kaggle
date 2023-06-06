import numpy as np
import matplotlib.pyplot as plt

# 画像の読み込み
saimg = np.load('sa.npy')

# RGBA画像をRGBに変換
rgb_img = saimg[:, :, :3]

# アルファチャンネルを取得
alpha_channel = saimg[:, :, 3]

# アルファチャンネルを考慮して画像を表示
plt.imshow(rgb_img)
plt.imshow(alpha_channel, cmap='gray', alpha=0.5)
plt.show()
