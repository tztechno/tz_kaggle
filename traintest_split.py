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

