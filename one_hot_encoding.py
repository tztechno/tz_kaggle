
import torch

# 例としてのdataYのデータ
dataY = torch.tensor([0, 1, 2, 1, 0])

# One-Hot Encodingの実行
num_classes = 3  # クラスの総数
one_hot = torch.zeros(dataY.size(0), num_classes)  # サイズを(データ数, クラス数)のゼロ行列で初期化

# scatterを使って、各データに対応するクラスの位置に1を設定する
one_hot.scatter_(1, dataY.unsqueeze(1), 1)

print(one_hot)
