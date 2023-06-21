############################################

from PIL import Image

image_path = 'path/to/image.jpg'
img = Image.open(image_path)
img.show()

############################################

import numpy as np
from PIL import Image

np_image = np.array([[255, 0, 0],
                     [0, 255, 0],
                     [0, 0, 255]], dtype=np.uint8)

pil_image = Image.fromarray(np_image)
pil_image.show()

############################################
