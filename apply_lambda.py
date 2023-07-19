anime_df["japanese_name"] = anime_df["japanese_name"].apply(lambda x:np.nan if x=="Unknown" else x)
