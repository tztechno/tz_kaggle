import pandas as pd

# DataFrameの作成
df = pd.DataFrame(columns=['A', 'B', 'C', 'D', 'E'], index=range(len(data)))

# 各行の数字を降順にソートし、結果をdf['order']列に入力する
df['order'] = df.apply(lambda row: ''.join(sorted(row, reverse=True)), axis=1)

print(df)
