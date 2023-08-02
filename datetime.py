
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

   # https://www.kaggle.com/code/lucasboesen/ensemble-cv-11-vs-lb-8-econ-data-google-trend
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df.date.dt.month.astype("int8")
    df['day_of_month'] = df.date.dt.day.astype("int8")
    df['day_of_year'] = df.date.dt.dayofyear.astype("int16")
    df['week_of_month'] = (df.date.apply(lambda d: (d.day-1) // 7 + 1)).astype("int8")
    df['week_of_year'] = (df.date.dt.weekofyear).astype("int8")
    df['day_of_week'] = (df.date.dt.dayofweek + 1).astype("int8")
    df['year'] = df.date.dt.year.astype("int32")
    df["is_wknd"] = (df.date.dt.weekday // 4).astype("int8")
    df["quarter"] = df.date.dt.quarter.astype("int8")
    df['is_month_start'] = df.date.dt.is_month_start.astype("int8")
    df['is_month_end'] = df.date.dt.is_month_end.astype("int8")
    df['is_quarter_start'] = df.date.dt.is_quarter_start.astype("int8")
    df['is_quarter_end'] = df.date.dt.is_quarter_end.astype("int8")
    df['is_year_start'] = df.date.dt.is_year_start.astype("int8")
    df['is_year_end'] = df.date.dt.is_year_end.astype("int8")
    # 0: Winter - 1: Spring - 2: Summer - 3: Fall
    df["season"] = np.where(df.month.isin([12,1,2]), 0, 1)
    df["season"] = np.where(df.month.isin([6,7,8]), 2, df["season"])
    df["season"] = pd.Series(np.where(df.month.isin([9, 10, 11]), 3, df["season"])).astype("int8")
    df['month_sin'] = np.sin(2*np.pi*df.month/12)
    df['month_cos'] = np.cos(2*np.pi*df.month/12)
    df['day_sin'] = np.sin(2*np.pi*df.day_of_month/31)
    df['day_cos'] = np.cos(2*np.pi*df.day_of_month/31)

####################################################
