import torch
import torchvision.transforms as T
normalize = T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
#normalized_image = normalize(image)
