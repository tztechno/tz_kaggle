
##############################################

#input_shape = (32,4000,3)
#output_shape = (32,250)

class MyCNN(nn.Module):
    def __init__(self):
        super(MyCNN, self).__init__()
        self.conv1 = nn.Conv2d(15, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.conv2 = nn.Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.conv3 = nn.Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.fc1 = nn.Linear(256 * 40 * 20, 250)

    def forward(self, x):
        print(x.shape)#torch.Size([32,4000,3])         
        x = x.view(-1,15,40,20)          
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = torch.relu(self.conv3(x))
        x = x.view(-1, 256 * 40 * 20)
        x = self.fc1(x)
        print(x.shape)
        return x  

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

#input_shape = (10,3,224,224)
#output_shape = (10,7)
class MyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1=nn.Conv2d(3,6,3,1)
        self.conv2=nn.Conv2d(6,16,3,1)
        self.fc1=nn.Linear(16*54*54,120) 
        self.fc2=nn.Linear(120,84)
        self.fc3=nn.Linear(84,20)
        self.fc4=nn.Linear(20,7)
    def forward(self,x):
        print(x.shape)#torch.Size([10, 3, 224, 224])
        x=F.relu(self.conv1(x))
        x=F.max_pool2d(x,2,2)
        print(x.shape)#torch.Size([10, 6, 111, 111])        
        x=F.relu(self.conv2(x))
        x=F.max_pool2d(x,2,2)
        print(x.shape)#torch.Size([10, 16, 54, 54])        
        x=x.view(-1,16*54*54)
        print(x.shape)#torch.Size([10, 46656])
        x=F.relu(self.fc1(x))
        print(x.shape)#torch.Size([10, 120])
        x=F.relu(self.fc2(x))
        x=F.relu(self.fc3(x))
        x=self.fc4(x)
        x=F.log_softmax(x,dim=1)
        print(x.shape)#torch.Size([10, 7])
        return x

 

########################################
      
