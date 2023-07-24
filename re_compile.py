train_df["text"].replace(re.compile(r'[\n\r\t]'), ' ', regex=True)

