
########################
import timm
import torch.nn as nn

model = timm.create_model('resnet18', pretrained=True)
model.fc = nn.Linear(in_features=model.fc.in_features, out_features=5, bias=True)

########################

class MyModel(nn.Module):

    def __init__(self, model_name='vit_base_patch8_224', pretrained=True):
        super(MyModel, self).__init__()
        self.model = timm.create_model(model_name, pretrained, in_chans=3)
        self.fc1 = nn.Linear(1000,16)
        self.fc2 = nn.Linear(16,64)        
        self.fc3 = nn.Linear(64,len(class_names))
        
    def forward(self, x):
        x = self.model(x)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x

########################
