
###########################

import torch

dataY = torch.tensor([0, 1, 2, 1, 0])
num_classes = 3
one_hot = torch.zeros(dataY.size(0), num_classes)
one_hot.scatter_(1, dataY.unsqueeze(1), 1)

print(one_hot)

###########################

dataY0=np.array(dataY0).astype(np.int64)
dataY = torch.eye(245)[dataY0]

###########################
