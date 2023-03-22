
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
