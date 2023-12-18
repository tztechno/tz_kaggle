from lightgbm.sklearn import LGBMRanker

ranker = LGBMRanker(
    objective="lambdarank",
    metric="map",
    boosting_type="dart",
    n_estimators=10,
    importance_type='gain',
    verbose=10
)

ranker = ranker.fit(
    train_X,
    train_y,
    group=train_baskets,
    eval_set = [(X_TEST, Y_TEST.values)],
    eval_group = test_baskets,
    eval_metric = 'map'
)
