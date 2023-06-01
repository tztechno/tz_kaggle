
###################################################

import numpy as np
from PIL import Image

image_path = 'path/to/image.jpg'
image = np.array(Image.open(image_path))
angle = 45

height, width = image.shape[:2]
center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

rotated_image = Image.fromarray(rotated_image)
rotated_image.show()

rotated_image.save('path/to/rotated_image.jpg')

###################################################

from PIL import Image

image_path = 'path/to/image.jpg'
image = Image.open(image_path)
angle = 45
rotated_image = image.rotate(angle)

rotated_image.save('path/to/rotated_image.jpg')
rotated_image.show()

###################################################
