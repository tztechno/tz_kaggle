import pandas as pd

# 'date'列を日付型に変換
train2['date'] = pd.to_datetime(train2['date'])

# 'date'列の型を確認
print(train2['date'].dtype)
