########################################

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
