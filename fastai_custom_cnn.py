

from fastai.vision.all import *

# Define your custom CNN architecture using PyTorch
class CustomCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 16 * 16, 512)
        self.fc2 = nn.Linear(512, 10)
    
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 64 * 16 * 16)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create a DataBlock for your data
dblock = DataBlock(blocks=(ImageBlock, CategoryBlock),
                   get_items=get_image_files,
                   splitter=RandomSplitter(),
                   get_y=parent_label,
                   item_tfms=Resize(224))

# Create a DataLoader for your data
dls = dblock.dataloaders('path/to/data')

# Create a Learner object using your custom CNN architecture
learn = vision_learner(dls, CustomCNN(), loss_func=CrossEntropyLossFlat(), metrics=accuracy)

# Train the model
learn.fit_one_cycle(10)

