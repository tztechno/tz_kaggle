##################################################

import cv2
import numpy as np

# 画像を読み込む
img = cv2.imread('input_image.jpg', 0)

# 画像を2値化する
thresh, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# 2値化された画像を反転する
reverse_img = np.logical_not(binary_img)

# 反転した画像を表示する
cv2.imshow('reverse', reverse_img.astype(np.uint8) * 255)
cv2.waitKey(0)
cv2.destroyAllWindows()

##################################################
