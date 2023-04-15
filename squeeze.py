
import numpy as np
import torch



data=np.random.rand(1,10,10, 3) 
print(data.shape)#(1, 10, 10, 3)

data2=np.squeeze(data)
print(data2.shape)#(10, 10, 3)

data3=np.expand_dims(data,axis=0)
print(data3.shape)#(1, 1, 10, 10, 3)



tdata=torch.randn(1,10,10, 3) 
print(tdata.shape)#torch.Size([1, 10, 10, 3])

tdata2=torch.squeeze(tdata)
print(tdata2.shape)#torch.Size([10, 10, 3])

tdata3=torch.unsqueeze(tdata,axis=0)
print(tdata3.shape)#torch.Size([1, 1, 10, 10, 3])
