###################################

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(4,128) 
        self.fc2 = nn.Linear(128,64) 
        self.fc3 = nn.Linear(64,128)
        self.fc4 = nn.Linear(128,64) 
        self.fc5 = nn.Linear(64,3) 

    def forward(self, x):
        x = self.fc1(x)      
        x = self.fc2(x)  
        x = self.fc3(x)       
        x = self.fc4(x)  
        x = self.fc5(x)     
        return x
      
################################### 
