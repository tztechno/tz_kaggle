##################################

from PIL import Image

def read_image(path):
    img = Image.open(path)
    img = img.convert("RGB")
    img = np.array(img)
    return img

##################################

import cv2

def read_image(path):
    img = cv2.imread(path)
    #print(img.shape)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (image_size, image_size))
    return img
  
##################################  
