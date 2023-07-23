pattern = r"(?:(\d+) hr.)? ?(?:(\d+) min.)?"
df[["hours", "minutes"]] = df["duration"].str.extract(pattern).fillna(0).astype(int)
