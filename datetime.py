
####################################################

import pandas as pd

# 'date'列を日付型に変換
train2['date'] = pd.to_datetime(train2['date'])

# 'date'列の型を確認
print(train2['date'].dtype)

####################################################

df["aired_start_date"] = df["aired"].apply(lambda x: pd.to_datetime(x.split("to")[0], errors="coerce"))
df["aired_end_date"] = df["aired"].apply(lambda x: pd.to_datetime(x.split("to")[-1], errors="coerce"))

####################################################
