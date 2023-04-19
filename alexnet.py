from torchvision import models

model = models.alexnet(pretrained=True)

model.classifier=nn.Sequential(   nn.Linear(9216,1024),
                                 nn.ReLU(),
                                 nn.Dropout(p=0.5),
                                 nn.Linear(1024,4),
                                 nn.LogSoftmax(dim=1))


'''
The list of models

AlexNet
VGG (VGG11, VGG13, VGG16, VGG19)
ResNet (ResNet18, ResNet34, ResNet50, ResNet101, ResNet152)
SqueezeNet (SqueezeNet1_0, SqueezeNet1_1)
DenseNet (DenseNet121, DenseNet169, DenseNet201, DenseNet161)
Inception (InceptionV3)
GoogLeNet (GoogLeNet)
ShuffleNet (ShuffleNetV2)
MobileNet (MobileNetV2)
EfficientNet (EfficientNet)

'''
