########################################

mean = np.array([0.485, 0.456, 0.406])
std = np.array([0.229, 0.224, 0.225])

normalized_image = normalize(image, mean, std)
print(normalized_image)

########################################

import torch
import torchvision.transforms as T
import numpy as np

img=cv2.imread(paths0[i])
images0+=[img]
img_tensor = torch.from_numpy(img).permute(1, 2, 0).float()
nor_image = normalize(img_tensor).permute(2, 0, 1)
images2+=[nor_image]

########################################

import torch
import torchvision.transforms as T
import numpy as np

normalize = T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

# Assuming you have a NumPy array image
image_np = np.random.rand(3, 224, 224)  # Example random image

# Convert the NumPy array image to a Torch tensor
image_tensor = torch.from_numpy(image_np)

# Add a batch dimension if the tensor doesn't have one
if len(image_tensor.shape) == 3:
    image_tensor = image_tensor.unsqueeze(0)

# Normalize the image tensor
normalized_image = normalize(image_tensor)

# Print the shape and range of the normalized image tensor
print(normalized_image.shape)
print(normalized_image.min(), normalized_image.max())

########################################
