
######################################################
[save as .pkl with fitted]

import joblib
import json

# モデルの保存
joblib.dump(clf, f'model_fold_{i}.pkl')  # 学習済みモデル全体を保存
with open(f'model_fold_{i}_params.json', 'w') as f:
    json.dump(clf.get_params(), f)  # パラメータをJSONに保存

# モデルの読み込み
clf = joblib.load(f'model_fold_{i}.pkl')  # 学習済みモデルの読み込み

# 予測の実行
preds = clf.predict(test_feat_df.values)
  
######################################################
[save as .model in lgbm, but not fitted]

import lightgbm as lgb
import json
from joblib import Parallel, delayed

def fit_lgb(X, y, cv, params: dict = None, n_jobs: int = 1):
    if params is None:
        params = {}

    models = []
    oof_pred = np.zeros_like(y, dtype=np.float32)

    def train_fold(i, idx_train, idx_valid):
        x_train, y_train = X[idx_train], y[idx_train]
        x_valid, y_valid = X[idx_valid], y[idx_valid]

        clf = lgb.LGBMRegressor(**params)
        clf.fit(
            x_train, y_train,
            eval_set=[(x_valid, y_valid)],
            verbose=False
        )

        pred_i = clf.predict(x_valid)
        oof_pred[idx_valid] = pred_i
        models.append(clf)

        # Save Booster and params to file
        clf.booster_.save_model(f'model_fold_{i}.model')  # Save Booster
        with open(f'model_fold_{i}_params.json', 'w') as f:
            json.dump(clf.get_params(), f)  # Save parameters to JSON

        return clf

    models = Parallel(n_jobs=n_jobs)(delayed(train_fold)(i, idx_train, idx_valid) for i, (idx_train, idx_valid) in enumerate(cv))

    return oof_pred, models

# モデルを読み込む関数
def load_models(num_folds):
    models = []
    for i in range(num_folds):
        # Load parameters
        with open(f'model_fold_{i}_params.json', 'r') as f:
            params = json.load(f)

        # Create a new LGBMRegressor with the saved params
        clf = lgb.LGBMRegressor(**params)
        
        # Load Booster model and assign it
        booster = lgb.Booster(model_file=f'model_fold_{i}.model')
        clf._Booster = booster  # Assign loaded Booster to LGBMRegressor
        models.append(clf)
    return models
  
######################################################
[save as .model in xgboost, catboost]

import xgboost as xgb
from joblib import Parallel, delayed

# Original fit_xgb function with modifications for saving models
def fit_xgb(X, y, cv, params: dict = None, n_jobs: int = 1):
    if params is None:
        params = {}

    models = []
    oof_pred = np.zeros_like(y, dtype=np.float32)

    def train_fold(i, idx_train, idx_valid):
        x_train, y_train = X[idx_train], y[idx_train]
        x_valid, y_valid = X[idx_valid], y[idx_valid]

        clf = xgb.XGBRegressor(**params)
        with Timer(prefix=f'fit fold={i} '):
            clf.fit(
                x_train, y_train,
                eval_set=[(x_valid, y_valid)],
            )

        pred_i = clf.predict(x_valid)
        oof_pred[idx_valid] = pred_i
        models.append(clf)

        # Save each fold's model to .model format
        clf.save_model(f'model_fold_{i}.model')

        return clf

    models = Parallel(n_jobs=n_jobs)(delayed(train_fold)(i, idx_train, idx_valid) for i, (idx_train, idx_valid) in enumerate(cv))

    return oof_pred, models

# Function to load models from .model files
def load_models(num_folds):
    models = []
    for i in range(num_folds):
        clf = xgb.XGBRegressor()
        clf.load_model(f'model_fold_{i}.model')  # Load each fold's model
        models.append(clf)
    return models

######################################################

######################################################
