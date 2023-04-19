from torchvision import models

alex= models.alexnet(pretrained=True)

alex.classifier=nn.Sequential(   nn.Linear(9216,1024),
                                 nn.ReLU(),
                                 nn.Dropout(p=0.5),
                                 nn.Linear(1024,4),
                                 nn.LogSoftmax(dim=1))

model=alex

