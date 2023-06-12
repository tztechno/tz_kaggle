    
########################################################

from torchvision import datasets, transforms, models 
from torchvision.datasets import ImageFolder
from torchvision.transforms import ToTensor
from torchvision.utils import make_grid
from torch.utils.data import random_split
from torch.utils.data.dataloader import DataLoader
import matplotlib.pyplot as plt


for images, labels in train_loader:
    fig, ax = plt.subplots(figsize=(18,10))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(make_grid(images,nrow=16).permute(1,2,0))
    break
    
########################################################
    
image_t=torch.from_numpy(image.reshape(1,image.shape[0],image.shape[1],image.shape[2]))
print(image_t.shape) # example input shape

images = torch.cat((image_t,image_t,image_t,
                     image_t,image_t,image_t,
                     image_t,image_t,image_t,), dim=0)

images=images.permute(0,3,1,2)
print(images.shape)

fig, ax = plt.subplots(figsize=(12,12))
ax.set_xticks([])
ax.set_yticks([])
ax.imshow(make_grid(images,nrow=3).permute(1,2,0))
    
########################################################
