
df = pd.read_csv('/kaggle/input/hubmap-hacking-the-human-vasculature/tile_meta.csv')
df = df.query('dataset != 3')
df.reset_index(inplace=True,drop=True)
df.head()
