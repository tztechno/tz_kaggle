####################################  
#first time
#clf = RandomForestRegressor()

#second time and after
with open('/kaggle/input/iris-species-random-forest-repeated/clf.pkl', 'rb') as f:
    clf = pickle.load(f)
ss = ShuffleSplit(n_splits=5,train_size=0.7,test_size =0.3,random_state=25) 

X=trainX.values
y=trainY.values

for train_index, test_index in ss.split(X):
    trainx, testx = X[train_index], X[test_index]
    trainy, testy = y[train_index], y[test_index]
    clf.fit(trainx,trainy) 
    print(clf.score(testx, testy))
    
with open('clf.pkl', 'wb') as f:
    pickle.dump(clf, f)    
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
