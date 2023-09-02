#####################################

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

#####################################

from PIL import Image
img = Image.open(path)
img.show()

#####################################

from IPython.display import Image, display
image_path = "/kaggle/input/animals10/raw-img/cavallo/OIP---MGqQIhmz3OEPYP-46_xwHaFj.jpeg"
display(Image(filename=image_path))

#####################################

import matplotlib.pyplot as plt
path= "/kaggle/input/animals10/raw-img/cavallo/OIP---MGqQIhmz3OEPYP-46_xwHaFj.jpeg"
image = plt.imread(path)
plt.imshow(image)
plt.axis('off')
plt.show()

#####################################
