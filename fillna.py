
import numpy as np

# Create a sample NumPy array with NaN values
arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# Create a masked array by identifying the NaN values
masked_arr = np.ma.masked_invalid(arr)

# Fill the masked values (NaN) with zeros
filled_arr = np.nan_to_num(masked_arr, nan=0)

# Output the filled array
print(filled_arr)

