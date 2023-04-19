
!pip install efficientnet_pytorch

from efficientnet_pytorch import EfficientNet

model = EfficientNet.from_pretrained('efficientnet-b0')

num_classes=4
# 最終層を置き換える
num_ftrs = model._fc.in_features
model._fc = nn.Linear(num_ftrs, num_classes)

# GPU が使用可能な場合は、GPU にモデルを転送する
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = model.to(device)

output = model(inputs)
