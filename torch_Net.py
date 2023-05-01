
###############################################################
class MyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = models.alexnet(pretrained=True)
        self.model.classifier = nn.Sequential( nn.Linear(9216,1024),
                                             nn.ReLU(),
                                             nn.Dropout(p=0.5),
                                             nn.Linear(1024,5),
                                             nn.LogSoftmax(dim=1))

    def forward(self, x):
        x = self.model(x)
        return x
###############################################################

#(224,224)
model= models.alexnet(pretrained=True)

for param in model.parameters():
    param.requires_grad=False

model.classifier=nn.Sequential( nn.Linear(9216,1024),
                                nn.ReLU(),
                                nn.Dropout(p=0.5),
                                nn.Linear(1024,len(class_names)),
                                nn.LogSoftmax(dim=1))

###############################################################
