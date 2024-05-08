
#########################################

import numpy as np

def convert_to_int_with_range_limit(value, min_value, max_value):
    int_value = int(value)
    int_value = np.clip(int_value, min_value, max_value)
    return int_value

#########################################

x = 101
print(np.clip(x, 0, 100))

#########################################

import numpy as np
x = 101
print(np.clip(x, 0, 100))    

#########################################

import torch
x = torch.tensor(101)
print(torch.clip(x, 0, 100))    

#########################################
