from surprise import Dataset
from surprise import KNNBasic

# トレーニングセットとテストセットのデータフレームを用意する
train_df  # トレーニングセットのデータフレーム
test_df  # テストセットのデータフレーム

# SurpriseのDatasetモジュールを使用してデータを読み込む
data = Dataset.load_from_df(train_df, reader=None)

# KNNBasicアルゴリズムを使ってモデルをトレーニングする
algo = KNNBasic()
trainset = data.build_full_trainset()  # トレーニングセットをSurpriseのTrainsetオブジェクトに変換
algo.fit(trainset)
