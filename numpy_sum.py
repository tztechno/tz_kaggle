#################################

import numpy as np

n = 5
arrays = [np.random.rand(1, 512, 512, 3) for _ in range(n)]
result = np.sum(arrays, axis=0)
print(result.shape)  # (1, 512, 512, 3)

#################################

MASKS = np.vstack([MASKS, np.array(masks)])

#################################

img_ex = np.expand_dims(img, axis=0)
MASKS = np.vstack([MASKS, img_ex])

#################################
