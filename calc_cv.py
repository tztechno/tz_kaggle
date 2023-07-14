import numpy as np

# 真の値と予測値のデータセット
true = np.array([1, 2, 3, 4, 5])
pred = np.array([1.2, 1.8, 2.9, 3.7, 4.9])

# 誤差の計算
errors = true - pred

# 平均値と標準偏差の計算
mean = np.mean(errors)
std = np.std(errors)

# CVの計算
cv = std / mean

print("CV:", cv)
