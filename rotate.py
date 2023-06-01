
###################################################

import numpy as np
from scipy import ndimage
angle = 45
r_img = ndimage.rotate(img, angle, reshape=False)
print(r_img.shape)
plt.imshow(r_img)
plt.axis('off')
plt.show()

###################################################

from PIL import Image

image_path = 'path/to/image.jpg'
image = Image.open(image_path)
angle = 45
rotated_image = image.rotate(angle)

rotated_image.save('path/to/rotated_image.jpg')
rotated_image.show()

###################################################
