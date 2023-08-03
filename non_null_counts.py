
#############################################################

non_null_counts = data0.count()
columns_of_small_nulls = non_null_counts[non_null_counts >= 1200].index
data1 = data0[columns_of_small_nulls]
display(data1.info())

#############################################################

import pandas as pd

# 一時的なデータフレームを作成する（テスト用）
data = {
    'column1': [1, 2, None, 4, None],
    'column2': [None, 6, None, 8, 9],
    'column3': [11, 12, 13, 14, 15],
    'column4': [16, None, 18, 19, 20]
}

df = pd.DataFrame(data)

# non-null総数が一定数以上のカラムをリストアップする関数
def list_columns_with_non_null(df, threshold):
    return [col for col in df.columns if df[col].count() >= threshold]

# 例として、non-null総数が3以上のカラムをリストアップする場合
threshold_value = 3
selected_columns = list_columns_with_non_null(df, threshold_value)

print(selected_columns)

#############################################################
