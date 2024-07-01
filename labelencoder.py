--------------------------------------------------------------------------
from sklearn.preprocessing import LabelEncoder

def labelencoder(df):
    for c in df.columns:
        if df[c].dtype=='object': 
            df[c] = df[c].fillna('N')
            lbl = LabelEncoder()
            lbl.fit(list(df[c].values))
            df[c] = lbl.transform(df[c].values)
    return df

--------------------------------------------------------------------------
from sklearn.preprocessing import LabelEncoder

def labelencoder(df_train, df_test):
    combined_df = pd.concat([df_train, df_test])
    for c in combined_df.columns:
        if combined_df[c].dtype == 'object':
            combined_df[c] = combined_df[c].fillna('N')
            lbl = LabelEncoder()
            lbl.fit(list(combined_df[c].values))
            combined_df[c] = lbl.transform(combined_df[c].values)
    return combined_df.iloc[:len(df_train)], combined_df.iloc[len(df_train):]

--------------------------------------------------------------------------
