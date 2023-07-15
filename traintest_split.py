########################

from sklearn.model_selection import train_test_split
trainx, validx, trainy, validy = train_test_split(trainX, trainY, test_size=0.2, random_state=42)

########################

n=len(info)
N=list(range(n))
random.shuffle(N)

train_ratio = 0.6
valid_ratio = 0.2
test_ratio = 0.2

train_size = int(train_ratio * n)
valid_size = int(valid_ratio * n)

train = N[:train_size]
valid = N[train_size:train_size+valid_size]
test = N[train_size+valid_size:]

########################

class DataModule(pl.LightningDataModule):
    def __init__(self, data, test_size=0.2, random_state=42):
        super().__init__()
        self.data = data
        self.test_size = test_size
        self.random_state = random_state
        
    def setup(self, stage=None):
        if stage == 'fit' or stage is None:
            train_data, val_data = train_test_split(self.data, test_size=self.test_size, random_state=self.random_state)
            self.train_data = DataSet(train_data)
            self.val_data = DataSet(val_data)
        
        if stage == 'test' or stage is None:
            self.test_data = DataSet(self.data)

    def train_dataloader(self):
        return DataLoader(self.train_data, batch_size=32, shuffle=True, num_workers=2)

    def val_dataloader(self):
        return DataLoader(self.val_data, batch_size=32, num_workers=2)

    def test_dataloader(self):
        return DataLoader(self.test_data, batch_size=32, num_workers=2)

########################

from sklearn.model_selection import train_test_split
path_label12,path_label3 = train_test_split(path_label0, test_size=0.2, random_state=42)
path_label1,path_label2 = train_test_split(path_label12, test_size=0.2, random_state=42)
print(len(path_label1),len(path_label2),len(path_label3))

########################

from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size=0.2, random_state=42)

########################

from sklearn.model_selection import train_test_split
train_data, test_data, train_labels, test_labels = train_test_split(df.data, df.target, test_size=0.2, random_state=42)

########################
import random

def split_train_test(n, test_ratio=0.2, seed=None):
    rng = random.Random(seed)
    indices = list(range(n))
    rng.shuffle(indices)
    test_size = int(n * test_ratio)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    return train_indices, test_indices
  
########################

import pandas as pd
import numpy as np

# データの読み込み
df = pd.read_csv('data.csv')

# データの分割
idx = np.random.permutation(len(df))
train_size = int(len(df) * 0.8)
train_idx, test_idx = idx[:train_size], idx[train_size:]
train_df, test_df = df.iloc[train_idx], df.iloc[test_idx]

########################

m=len(data)
M=list(range(m))
random.seed(2021)
random.shuffle(M)

train=data.iloc[M[0:(m//5)*4]]
test=data.iloc[M[(m//5)*4:]]

########################

import torch
from torch.utils.data import random_split

# データセットを作成するコード（例）
dataset = YourDataset()

# データセットのサイズを取得
dataset_size = len(dataset)

# train、validation、testの割合を設定
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# データセットを分割するためのインデックスを計算
train_size = int(train_ratio * dataset_size)
val_size = int(val_ratio * dataset_size)
test_size = dataset_size - train_size - val_size

# データセットをランダムに分割
train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])

# 分割後のデータセットのサイズを確認
print("Train dataset size:", len(train_dataset))
print("Validation dataset size:", len(val_dataset))
print("Test dataset size:", len(test_dataset))

########################
