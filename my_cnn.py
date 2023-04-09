
#########################################################
#input torch.Size([32, 4000, 3])
#output torch.Size([32, 250])

class MyCNN(nn.Module):
    def __init__(self):
        super(MyCNN, self).__init__()
        self.conv1_weights = nn.Parameter(torch.randn(64, 3, 3))
        self.conv1_bias = nn.Parameter(torch.randn(64))
        self.conv2_weights = nn.Parameter(torch.randn(128, 64, 3))
        self.conv2_bias = nn.Parameter(torch.randn(128))
        self.conv3_weights = nn.Parameter(torch.randn(256, 128, 3)) 
        self.conv3_bias = nn.Parameter(torch.randn(256)) 
        self.fc1 = nn.Linear(128000, 250) 

    def forward(self, x):
        batch_size = x.size(0)
        x = x.permute(0, 2, 1) 
        x = F.conv1d(x, self.conv1_weights, bias=self.conv1_bias, stride=1, padding=1)
        x = F.relu(x)
        x = F.max_pool1d(x, 2)
        x = F.conv1d(x, self.conv2_weights, bias=self.conv2_bias, stride=1, padding=1)
        x = F.relu(x)
        x = F.max_pool1d(x, 2)
        x = F.conv1d(x, self.conv3_weights, bias=self.conv3_bias, stride=1, padding=1)
        x = F.relu(x)
        x = F.max_pool1d(x, 2)
        x = x.view(batch_size, -1) 
        x = self.fc1(x) 
        return x

#########################################################
#input torch.Size([32, 4000, 3])
#output torch.Size([32])

class MyCNN(nn.Module):
    def __init__(self, num_classes=245):
        super(MyCNN, self).__init__()
        self.conv1 = nn.Conv1d(3, 32, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.maxpool = nn.MaxPool1d(kernel_size=16)
        self.fc = nn.Linear(32*250, num_classes)

    def forward(self, x):
        x = x.permute(0,2,1) 
        x = self.conv1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        return x.squeeze()
    
#########################################################
#input torch.Size([16, 3, 100, 100])
#output torch.Size([16, 4])

class MyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(64 * 25 * 25, 128)
        self.fc2 = nn.Linear(128, 4)

    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 64 * 25 * 25)
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x

#########################################################
#input torch.Size([16, 3, 400, 400])
#output torch.Size([16, 250])

class MyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(128 * 25 * 25, 256)
        self.fc2 = nn.Linear(256, 250)

    def forward(self, x):
        x = self.pool1(nn.functional.relu(self.conv1(x)))
        x = self.pool2(nn.functional.relu(self.conv2(x)))
        x = self.pool3(nn.functional.relu(self.conv3(x)))
        x = x.view(-1, 128 * 25 * 25)
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x

############################################################
#input torch.Size([16, 3, 128, 128])
#output torch.Size([16, 5])

import torch.nn as nn

class MyCNN(nn.Module):
    def __init__(self):
        super(MyCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.dropout = nn.Dropout(p=0.5)
        self.fc1 = nn.Linear(128 * 16 * 16, 512)
        self.fc2 = nn.Linear(512, 5)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.pool(x)
        x = self.conv3(x)
        x = self.relu(x)
        x = self.pool(x)
        x = self.dropout(x)
        x = x.view(-1, 128 * 16 * 16)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        
        return x


############################################################
