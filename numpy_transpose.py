import numpy as np

array1 = np.zeros((256, 256, 8))
transposed_array = np.transpose(array1, (2, 0, 1))
array2 = transposed_array.reshape((8, 256, 256, 1))
