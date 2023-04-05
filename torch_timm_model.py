
import timm
import torch.nn as nn

model = timm.create_model('resnet18', pretrained=True)
model.fc = nn.Linear(in_features=model.fc.in_features, out_features=5, bias=True)


