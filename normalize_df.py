from sklearn.preprocessing import MinMaxScaler

def normalize_df(df):
    scaler = MinMaxScaler()
    normalized = scaler.fit_transform(df)
    df = pd.DataFrame(normalized, columns=df.columns)
    return df
