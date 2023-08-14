
############################################################

import cv2
import numpy as np
import matplotlib.pyplot as plt

image0=cv2.imread(path0)
image0 = cv2.cvtColor(image0, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(3,3))
plt.imshow(image0)
plt.axis('off')
plt.show()

image = cv2.imread(path0, cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
pixels = np.argwhere(hsv>0)
all_colors = {tuple(image[pixel[0], pixel[1]]) for pixel in pixels}
print("All colors:", all_colors)

for c in all_colors:
    print(c)
    nc= [np.array(c)]
    plt.figure(figsize=(2,2))
    plt.imshow([nc])
    plt.axis('off')
    plt.show()

############################################################

lower_color = (255, 0, 0)
upper_color = (255, 0, 0)
mask = cv2.inRange(image, lower_color, upper_color)
focus = cv2.bitwise_and(image, image, mask=mask)
plt.figure(figsize=(3,3))
plt.imshow(focus)
plt.axis('off')
plt.show()

############################################################
