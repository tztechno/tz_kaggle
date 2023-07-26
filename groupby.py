import pandas as pd

# サンプルデータフレームの作成
data = {
    'category': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'value': [10, 15, 5, 8, 12, 9, 6, 7]
}
df = pd.DataFrame(data)

# 'category'列を基準にグループ化し、'value'列の平均、最大、最小を同時に算出する
result = df.groupby('category')['value'].agg(['mean', 'max', 'min'])

print(result)
