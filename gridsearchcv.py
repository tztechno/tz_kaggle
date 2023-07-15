
###############################################################

from sklearn.model_selection import GridSearchCV

#LightGBMモデル(gbm3)を初期化します。
gbm3 = lgb.LGBMClassifier(objective='binary')

#ハイパーパラメータのグリッド検索:
reg_cv = GridSearchCV(gbm3,{'reg_alpha':[0.0001,0.0002,0.0004,0.0008,0.0016],
                            'reg_lambda':[0.01,0.02,0.04,0.08,0.16]},verbose=1)
#GridSearchCVのfitメソッドを使用して、グリッドサーチを実行します。
reg_cv.fit(X_train,Y_train)

#新しいモデル(gbm3)に対して、fitメソッドを使用してトレーニングを行います。
gbm3 = lgb.LGBMClassifier(**reg_cv.best_params_)
gbm3.fit(X_train,Y_train)

y_pred3 = gbm3.predict(np.array(X_test))

sub = gender_submission
sub['Survived'] = list(map(int, y_pred3))
sub.to_csv("submission3.csv", index=False)
sub

###############################################################

from sklearn.model_selection import GridSearchCV

# パラメータグリッドの定義
param_grid = {'ensemble_ratio': [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]}

# GridSearchCVの設定
grid_search = GridSearchCV(estimator=YourModel(), param_grid=param_grid, scoring='neg_mean_squared_error', cv=5)

# モデルの学習と最適なパラメータの探索
grid_search.fit(X, y)

# 最適なパラメータとそのスコアの表示
print("Best Ensemble Ratio:", grid_search.best_params_['ensemble_ratio'])
print("Best RMSE:", np.sqrt(-grid_search.best_score_))

###############################################################
