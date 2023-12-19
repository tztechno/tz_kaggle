import polars as pl

# データフレームの作成
df = pl.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'San Francisco', 'Los Angeles']
})

# データフレームの表示
print(df)

# 特定の列の選択
selected_columns = df[['name', 'age']]
print(selected_columns)

# データのフィルタリング
filtered_data = df.filter(df['age'] > 30)
print(filtered_data)

# データのグループ化と集計
grouped_data = df.groupby('city').agg({'age': 'mean'})
print(grouped_data)
