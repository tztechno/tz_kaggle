#############################################################

from joblib import Parallel, delayed

# 例として、重い計算をする関数を定義
def heavy_computation(x):
    return x ** 2

# 複数の入力値に対して、関数を並列実行
results = Parallel(n_jobs=4)(delayed(heavy_computation)(i) for i in range(10))
print(results)

----------------------------
tasks = [delayed(heavy_computation)(i) for i in range(10)]
results = Parallel(n_jobs=4)(tasks)
print(results)
----------------------------
tasks=[]
for i in range(10):
    tasks.append(delayed(heavy_computation)(i))
results = Parallel(n_jobs=4)(tasks)
print(results)
----------------------------
#############################################################


from joblib import Parallel, delayed


def fit_lgb(X, y, cv, params: dict = None, n_jobs: int = 1):
    if params is None:
        params = {}

    models = []
    oof_pred = np.zeros_like(y, dtype=np.float32) 

    def train_fold(i, idx_train, idx_valid):
        x_train, y_train = X[idx_train], y[idx_train]
        x_valid, y_valid = X[idx_valid], y[idx_valid]

        clf = clf = lgb.LGBMRegressor(**params)
        with Timer(prefix=f'fit fold={i} '):
            clf.fit(
                x_train, y_train,
                eval_set=[(x_valid, y_valid)],
            )

        pred_i = clf.predict(x_valid)
        oof_pred[idx_valid] = pred_i
        models.append(clf)
        return clf

    models = Parallel(n_jobs=n_jobs)(delayed(train_fold)(i, idx_train, idx_valid) for i, (idx_train, idx_valid) in enumerate(cv))

    weights2=weights[0:len(y)]
    r2_score=weighted_zero_mean_r2(y, oof_pred, weights2)

    print('-' * 50)
    print('FINISHED | r2_score: {:.4f}'.format(r2_score))
    return oof_pred, models


#############################################################
    former style
    
    def fit_lgb(X, y, cv, 
                 params: dict=None):

        if params is None:
            params = {}

        models = []
        oof_pred = np.zeros_like(y, dtype=float)

        for i, (idx_train, idx_valid) in enumerate(cv): 
            x_train, y_train = X[idx_train], y[idx_train]
            x_valid, y_valid = X[idx_valid], y[idx_valid]

            clf = lgb.LGBMRegressor(**params)

            with Timer(prefix='fit fold={} '.format(i)):
                clf.fit(x_train, y_train, 
                        eval_set=[(x_valid, y_valid)])

            pred_i = clf.predict(x_valid)
            oof_pred[idx_valid] = pred_i
            models.append(clf)

        weights2=weights[0:len(y)]
        r2_score=weighted_zero_mean_r2(y, oof_pred, weights2)

        print('-' * 50)
        print('FINISHED | r2_score: {:.4f}'.format(r2_score))
        return oof_pred, models


#############################################################
