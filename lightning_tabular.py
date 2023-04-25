
#Iris Pytorch Lightning Linear　

import re
import random
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, confusion_matrix, auc
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, Dataset
from torch import optim
from torch.optim import lr_scheduler
import pytorch_lightning as pl


class IrisClassifier(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(4,128), 
            nn.Linear(128,64),
            nn.Linear(64,128),
            nn.Linear(128,64), 
            nn.Linear(64,3),                  
        )

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.cross_entropy(y_hat, y)
        self.log('train_loss', loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.cross_entropy(y_hat, y)
        self.log('val_loss', loss)
        return loss

    def test_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.cross_entropy(y_hat, y)
        pred = torch.argmax(y_hat, dim=1)
        acc = accuracy_score(pred, y)
        self.log('test_loss', loss)
        self.log('test_acc', acc)  

    def configure_optimizers(self):
        optimizer = optim.Adam(self.parameters(), lr=1e-3)
        return optimizer  
      
# define the dataset class
class IrisDataSet(Dataset):
    def __init__(self, data):
        dataY=data['Species']
        dataX=data.drop(['Id','Species'],axis=1)
        self.data = data
        self.dataX = dataX
        self.dataY = dataY
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.dataX.iloc[index].values.astype(np.float32), self.dataY.iloc[index]
      
# define the datamodule class
class IrisDataModule(pl.LightningDataModule):
    def __init__(self, data):
        super().__init__()
        self.dataset = IrisDataSet(data)
        
    def setup(self, stage=None):
        if stage == 'fit' or stage is None:
            self.train_data, self.val_data = train_test_split(self.dataset, test_size=0.3, random_state=42)
        
        if stage == 'test' or stage is None:
            self.test_data = self.dataset

    def train_dataloader(self):
        return DataLoader(self.train_data, batch_size=32, shuffle=True, num_workers=2)

    def val_dataloader(self):
        return DataLoader(self.val_data, batch_size=32, num_workers=2)

    def test_dataloader(self):
        return DataLoader(self.test_data, batch_size=32, num_workers=2)
      
# define the data
data0 = pd.read_csv("/kaggle/input/iris/Iris.csv")
m=len(data0)
M=list(range(m))
random.seed(2022)
random.shuffle(M)
data=data0.iloc[M]

# map label to int
Name0=data['Species'].unique().tolist()
Name=sorted(Name0)
N=list(range(len(Name)))
normal_mapping=dict(zip(Name,N)) 
reverse_mapping=dict(zip(N,Name))
data['Species']=data['Species'].map(normal_mapping)

# define datamodule
datamodule = IrisDataModule(data)

# train the model
model = IrisClassifier()
trainer = pl.Trainer(max_epochs=600)
trainer.fit(model, datamodule)

# test the model
datamodule.setup(stage='test')
test_loader = datamodule.test_dataloader()
trainer.test(dataloaders=test_loader)

#classification_report
test_pred = []
test_true = []
model.eval()
with torch.no_grad():
    for batch in test_loader:
        x, y = batch
        y_pred = model(x)
        test_pred.extend(y_pred.argmax(dim=1).tolist())
        test_true.extend(y.tolist())
print(classification_report(test_true,test_pred,target_names=Name,digits=4))



 
 
 
 
 
 
