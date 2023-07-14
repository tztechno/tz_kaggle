

################################

from surprise import Dataset
from surprise import KNNBasic

train_df  # トレーニングセットのデータフレーム
test_df  # テストセットのデータフレーム

# SurpriseのDatasetモジュールを使用してデータを読み込む
data = Dataset.load_from_df(train_df, reader=None)

# KNNBasicアルゴリズムを使ってモデルをトレーニングする
algo = KNNBasic()
trainset = data.build_full_trainset()  # トレーニングセットをSurpriseのTrainsetオブジェクトに変換
algo.fit(trainset)


################################

from surprise.prediction_algorithms import (
    BaselineOnly,
    CoClustering,
    KNNBaseline,
    KNNBasic,
    KNNWithMeans,
    NMF,
    NormalPredictor,
    SlopeOne,
    SVD,
    SVDpp,
)

################################
