###########################

import pandas as pd

# 列情報
data = ['A', 'B', 'C']

# データフレームの作成
df = pd.DataFrame({'column': data})

# ダミー変数の one-hot encoding を作成
one_hot_encoding = pd.get_dummies(df['column'])

print(one_hot_encoding)

###########################
# 列情報
data = 'ABC'

# ユニークな要素のリストを作成
unique_elements = list(set(data))

# one-hot encoding のためのゼロで初期化された配列を作成
one_hot_encoding = np.zeros((len(data), len(unique_elements)))

# 各要素に対して one-hot encoding を適用
for i, element in enumerate(data):
    element_index = unique_elements.index(element)
    one_hot_encoding[i, element_index] = 1

print(one_hot_encoding)

###########################

import numpy as np

categorical_data = np.array([1, 2, 3])
unique_values = np.unique(categorical_data)
one_hot_data = np.eye(len(unique_values))[categorical_data]
one_hot_data2=one_hot_data.reshape(-1,len(unique_values))

###########################

import torch

dataY = torch.tensor([0, 1, 2, 1, 0])
num_classes = 3
one_hot = torch.zeros(dataY.size(0), num_classes)
one_hot.scatter_(1, dataY.unsqueeze(1), 1)

print(one_hot)

###########################

dataY0=np.array(dataY0).astype(np.int64)
dataY = torch.eye(245)[dataY0]

###########################

from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import MultiLabelBinarizer

multilabel_cols = ["genres", "producers", "licensors", "studios"]
multilabel_dfs = []
n_components=10
for c in multilabel_cols:
    list_srs = anime_df[c].map(lambda x: x.split(", ")).tolist()

    mlb = MultiLabelBinarizer()
    ohe_srs = mlb.fit_transform(list_srs)
    if c == "genres" or c == "licensors":
        # ユニーク数が多くないのでOne-hot表現のまま
        col_df = pd.DataFrame(ohe_srs, columns=[f"ohe_{c}_{name}" for name in mlb.classes_])
    else:
        # ユニーク数が多いので、SVDで次元圧縮する
        svd = TruncatedSVD(n_components=10)
        svd_arr = svd.fit_transform(ohe_srs)
        col_df = pd.DataFrame(
            svd_arr,
            columns=[f"svd_{c}_{ix}" for ix in range(n_components)]
        )
    multilabel_dfs.append(col_df)

multilabel_df = pd.concat(multilabel_dfs, axis=1)
display(multilabel_df[0:10].T)

###########################
