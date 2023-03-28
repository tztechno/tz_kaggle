
import pandas as pd

# DataFrameの作成
df = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'one', 'two', 'two', 'one'],
                   'C': [1, 2, 3, 4, 5, 6],
                   'D': [2, 4, 6, 8, 10, 12]})

# ピボットテーブルの作成
pivot_table = df.pivot(index='A', columns='B', values='C')

# ピボットテーブルの表示
print(pivot_table)
