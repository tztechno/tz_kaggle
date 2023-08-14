import pandas as pd

# データを作成
data1 = {'Value1': [10, 20, 30]}
data2 = {'Value2': [200, 300, 400]}

df1 = pd.DataFrame(data1, index=[1, 2, 3])
df2 = pd.DataFrame(data2, index=[2, 3, 4])

# インデックスを使用してマージ
merged_df = pd.merge(df1, df2, left_index=True, right_index=True, how='outer')

# df2に存在しない行を表示
missing_rows = merged_df[merged_df['Value2'].isnull()]
print(missing_rows)
