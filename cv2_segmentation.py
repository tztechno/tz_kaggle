
import cv2
import matplotlib.pyplot as plt

# 画像を読み込む
img = cv2.imread(path1)

# 画像の色空間をBGRからRGBに変換する
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

# セグメンテーションデータを適用する
mask = np.array(segmentation_data)
mask = mask.astype(np.uint8)

# 画像に塗りつぶしを適用する
filled_image = cv2.fillPoly(img, [mask], (0, 0, 255))

# 結果の画像を表示する
plt.imshow(filled_image)
plt.show()

