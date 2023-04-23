
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
