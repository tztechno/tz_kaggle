train_df["text"].replace(re.compile(r'[\n\r\t]'), ' ', regex=True)

#改行文字（\n）や復帰文字（\r）やタブ文字（\t）をスペースに置換する処理
