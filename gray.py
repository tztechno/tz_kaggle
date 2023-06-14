########################################################

import cv2

def convert_to_gray(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray_image.jpg", gray_image)
    
convert_to_gray("input_image.jpg")

########################################################

from PIL import Image

def convert_to_gray(image_path):
    image = Image.open(image_path)
    gray_image = image.convert("L")
    gray_image.save("gray_image.jpg")
    
convert_to_gray("input_image.jpg")

########################################################
