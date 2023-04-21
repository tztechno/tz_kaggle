
######################################################
#create dataset from df of path/label

import torch
from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self, data_df):
        self.data_df = data_df
    
    def __len__(self):
        return len(self.data_df)
    
    def __getitem__(self, idx):
        path, label = self.data_df.iloc[idx]
        img = Image.open(os.path.join(dir0,path)).convert('RGB')
        img = img.resize((224, 224))
        img = torch.tensor(np.array(img)).permute(2, 0, 1).float() / 255.0
        
        return img, label
    
######################################################

import torch
from torch.utils.data import Dataset

data = torch.randn(640,3,40,40)
labels = torch.randint(0,3,size=(640,))

class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        sample = {'data': self.data[idx], 'label': self.labels[idx]}
        return sample

# データセットを作成する
dataset = MyDataset(data, labels)

######################################################

