algo = KNNBasic

param_grid = { 'k': [5,10,15,20,50], 'min_k': [2,3,4,5] }
gs = GridSearchCV(algo, param_grid, cv=5)
gs.fit(data)

print()
print(gs.best_params)
best_algo = KNNBasic(k=gs.best_params['rmse']['k'], min_k=gs.best_params['rmse']['min_k'])
print(best_algo.k, best_algo.min_k)
