####################################  

import pickle
import lightgbm as lgbm

# 学習データを用意する
X_train, y_train = ...

# モデルを定義する
params = {...}
clf = lgbm.LGBMRegressor(**params)

# モデルを学習する
clf.fit(X_train, y_train)

# 学習済みのモデルを保存する
with open('clf.pkl', 'wb') as f:
    pickle.dump(clf, f)

####################################  
  
import pickle

# 学習済みのモデルを読み込む
with open('clf.pkl', 'rb') as f:
    clf = pickle.load(f)

# モデルを使用する
X_test = ...
y_pred = clf.predict(X_test)

####################################  
