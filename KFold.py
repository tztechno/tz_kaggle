
######################################################

import numpy as np
from sklearn.model_selection import KFold, GroupKFold
from sklearn.linear_model import LinearRegression

# サンプルデータ生成
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]])
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# 各サンプルの所属するグループを示す配列
groups = np.array([1, 1, 1, 1, 2, 2, 2, 2, 2, 2])

######################################################

# KFoldを使って交差検証を行う場合
kf = KFold(n_splits=5, shuffle=True, random_state=42)

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # モデルを訓練
    model = LinearRegression()
    model.fit(X_train, y_train)

    # モデルの評価
    score = model.score(X_test, y_test)
    print("KFold Score:", score)

######################################################

# GroupKFoldを使って交差検証を行う場合
gkf = GroupKFold(n_splits=2)

for train_index, test_index in gkf.split(X, y, groups):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # モデルを訓練
    model = LinearRegression()
    model.fit(X_train, y_train)

    # モデルの評価
    score = model.score(X_test, y_test)
    print("GroupKFold Score:", score)

######################################################
# データを用意する（Xは特徴量行列、yは対応するラベル）

from sklearn.model_selection import KFold
kf = KFold(n_splits=k)  # kはフォールドの数
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    

from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=k)  # kはフォールドの数
for train_index, test_index in skf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]


from sklearn.model_selection import GroupKFold
gkf = GroupKFold(n_splits=k)  # kはフォールドの数
for train_index, test_index in gkf.split(X, y, groups):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]


from sklearn.model_selection import StratifiedGroupKFold
sgkf = StratifiedGroupKFold(n_splits=k)  # kはフォールドの数
for train_index, test_index in sgkf.split(X, y, groups):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
######################################################

