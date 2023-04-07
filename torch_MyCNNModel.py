##############################################

## input (32, 224, 224, 3) 
## output (32, 5)

class MyCNNModel(nn.Module):
    def __init__(self):
        super(MyCNNModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 56 * 56, 512)
        self.fc2 = nn.Linear(512, 5)
        
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))  # Conv1 -> ReLU -> MaxPool
        x = self.pool(F.relu(self.conv2(x)))  # Conv2 -> ReLU -> MaxPool
        x = x.view(-1, 64 * 56 * 56)          # Flatten
        x = F.relu(self.fc1(x))               # Fully connected layer 1 -> ReLU
        x = self.fc2(x)                       # Fully connected layer 2 (output)
        return x
    
############################################## 

## input (32, 784) 
## output (32, 10)

class MyCNN(nn.Module):
    def __init__(self):
        super(MyCNN, self).__init__()
        self.conv1 = nn.Conv1d(1, 32, kernel_size=5, stride=1)
        self.fc1 = nn.Linear(32*780, 10)

    def forward(self, x):
        x = x.view(x.size(0), 1, 32, 784)  # 入力データのサイズを変更
        x = self.conv1(x)
        x = x.view(x.size(0), -1)  # データを1次元に変換
        x = self.fc1(x)
        return x
    
 ##############################################    
