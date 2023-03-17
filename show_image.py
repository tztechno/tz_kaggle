import cv2
import matplotlib.pyplot as plt

def show_image(path):
    img = cv2.imread(path)
    img = img[...,::-1] # bgr => rgb
    plt.figure(figsize=(6, 6))
    plt.imshow(img)
    plt.axis('OFF')
    plt.show()
    return img
