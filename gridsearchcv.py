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
