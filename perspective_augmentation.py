import cv2
import numpy as np

#自由設定
def perspective_augmentation(image, top_left, top_right, bottom_right, bottom_left):
    height, width = image.shape[:2]
    src_points = np.float32([top_left, top_right, bottom_right, bottom_left])
    dst_points = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    augmented_image = cv2.warpPerspective(image, perspective_matrix, (width, height))
    return augmented_image

#上からの図
def perspective_augmentation(image, scale=0.5, shear_range=10):
    height, width = image.shape[:2]
    src_points = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    dst_points = np.float32([[0, 0], [width, 0], [width * scale, height], [width * (1 - scale), height]])
    perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    augmented_image = cv2.warpPerspective(image, perspective_matrix, (width, height))
    return augmented_image

# 画像を読み込みます
image = cv2.imread('input.jpg')
# 透視変換を適用します
augmented_image = perspective_augmentation(image, scale=0.5, shear_range=10)
# 変換後の画像を表示します
cv2.imshow('Augmented Image', augmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
