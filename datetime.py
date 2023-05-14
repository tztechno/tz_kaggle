# 'date'列をdatetime64型に変換
df['date'] = pd.to_datetime(df['date'])
