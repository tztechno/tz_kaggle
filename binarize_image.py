####################################################################

img = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img=binarize_image(img, threshold)

####################################################################

import numpy as np

def binarize_image(image, threshold):
    binary_image = np.where(image >= threshold, 255, 0)
    return binary_image.astype(np.uint8)

image_data = np.random.randint(0, 256, size=(5, 5), dtype=np.uint8)

threshold = 128
binary_image_data = binarize_image(image_data, threshold)

####################################################################

def binarize_image(image, threshold):
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

threshold_value = 127

####################################################################

import torchvision.transforms.functional as F
from PIL import Image

def binarize(image, threshold):
    """
    Args:
        image (PIL.Image): 二値化する画像。
        threshold (float): 二値化の閾値。
    Returns:
        PIL.Image: 二値化された画像。
    """
    image = image.convert("L")  # 画像をグレースケールに変換
    image = F.to_tensor(image)  # テンソルに変換
    image = (image > threshold).float()  # 閾値を用いて二値化
    image = F.to_pil_image(image)  # PIL画像に変換
    return image

####################################################################
