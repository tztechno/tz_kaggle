from sklearn.metrics import mean_absolute_error
import lightgbm as lgbm
from sklearn.model_selection import KFold

fold = KFold(n_splits=5, shuffle=True, random_state=510)
cv = list(fold.split(feat_train_df.values, train_df["x_0"].values))

def fit_lgbm(X, 
             y, 
             cv, 
             params: dict=None, 
             verbose: int=1000):
    """lightGBM を CrossValidation の枠組みで学習を行なう function"""

    # パラメータがないときは、空の dict で置き換える
    if params is None:
        params = {}

    models = []
    n_records = len(X)
    # training data の target と同じだけのゼロ配列を用意
    oof_pred = np.zeros((n_records, ), dtype=np.float32)

    for i, (idx_train, idx_valid) in enumerate(cv): 
        # この部分が交差検証のところです。データセットを cv instance によって分割します
        # training data を trian/valid に分割
        x_train, y_train = X[idx_train], y[idx_train]
        x_valid, y_valid = X[idx_valid], y[idx_valid]

        clf = lgbm.LGBMRegressor(**params)

        with Timer(prefix="fit fold={} ".format(i)):
            clf.fit(x_train, y_train, 
                    eval_set=[(x_valid, y_valid)],  
                    
                    # 前回の tutorial では古い書き方でした。
                    # 今回はあたらしいAPIに対応して earlystopping / log 出力を callback で記載しています.
                    callbacks=[
                      lgbm.early_stopping(stopping_rounds=100, verbose=True),
                      lgbm.log_evaluation(period=verbose),
                    ])

        pred_i = clf.predict(x_valid)
        oof_pred[idx_valid] = pred_i
        models.append(clf)

        # 今回の指標の MAE で計算する
        score = mean_absolute_error(y_valid, pred_i, )
        print(f" - fold{i + 1} - {score:.4f}")

    return oof_pred, models
