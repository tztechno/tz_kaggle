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
