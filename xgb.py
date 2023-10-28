import xgboost as xgb

params = {
    'objective': 'binary:logistic',  # 2値分類の場合
    'eval_metric': 'logloss',        # 評価メトリクスは交差エントロピー
    'max_depth': 3,                  # 木の深さ
    'learning_rate': 0.1,           # 学習率
    'n_estimators': 100,             # ブースティングのラウンド数
    'subsample': 0.8,               # サンプリングの割合
    'colsample_bytree': 0.8,        # 列のサンプリングの割合
    'reg_alpha': 0.01,              # L1 正則化
    'reg_lambda': 1.0,              # L2 正則化
    'scale_pos_weight': 1,          # 正例と負例の重みのバランス
}

# XGBoostモデルを構築
model = xgb.XGBClassifier(**params)
