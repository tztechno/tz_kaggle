##################################################
#RGBAの画像を保存する時、BGRAに変わるのを防止する

img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGBA)
cv2.imwrite('electric_sign.png',img4)

#動作不良...
cv2.imwrite('electric_sign.png',img4, cv2.IMWRITE_COLOR_BGR2RGBA)

##################################################

import cv2
import numpy as np
import matplotlib.pyplot as plt

path='xxx.jpg'
img=cv2.imread(path)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=cv2.resize(img,dsize=None,fx=0.1,fy=0.1)
plt.imshow(img)
plt.show()

##################################################

import cv2
import numpy as np

img = cv2.imread('input_image.jpg', 0)
thresh, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
reverse_img = np.logical_not(binary_img)

cv2.imshow('reverse', reverse_img.astype(np.uint8) * 255)
cv2.waitKey(0)
cv2.destroyAllWindows()

##################################################

import cv2

img = cv2.imread('input_image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

##################################################

import cv2
import numpy as np

image = cv2.imread("image.jpg")
mask = cv2.imread("mask.png", 0)  # 0はグレースケールで読み込むことを指定する
_, mask = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

fg = cv2.bitwise_and(image, image, mask=mask)
bg = cv2.bitwise_and(image, image, mask=mask_inv)
result = cv2.add(fg, bg)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

##################################################




