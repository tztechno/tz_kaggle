import numpy as np

# 0から2までの整数値をランダムに生成して100個のデータを作成
y_true = np.random.randint(0, 3, 100)
y_pred = np.random.randint(0, 3, 100)

print("y_true:", y_true)
print("y_pred:", y_pred)
