from sklearn.neighbors import NearestNeighbors

# データを用意する（例として2次元のデータを使用）
data = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

# 最近傍点の数を指定
k_neighbors = 2

# NearestNeighborsモデルを作成
nn_model = NearestNeighbors(n_neighbors=k_neighbors)

# データをモデルにフィットさせる
nn_model.fit(data)

# 最近傍点を探す対象のデータポイントを指定
query_point = [[2, 3]]

# 最近傍点を検索
distances, indices = nn_model.kneighbors(query_point)

print("最近傍点のインデックス:", indices)
print("最近傍点までの距離:", distances)
