import numpy as np

# 例としてランダムな2つの画像を生成する
img1 = np.random.rand(100, 100, 3)  # 100x100のRGB画像
img2 = np.random.rand(100, 100, 3)  # 100x100のRGB画像

# 2つの画像を縦に結合する
result = np.vstack((img1, img2))

# 結果のサイズを確認する
print(result.shape)  # 出力: (200, 100, 3)
