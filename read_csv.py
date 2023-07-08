import chardet

with open("/kaggle/input/horse-racing-results-2017-2020/Horse Racing Results.CSV", 'rb') as f:
    result = chardet.detect(f.read())

data0 = pd.read_csv("/kaggle/input/horse-racing-results-2017-2020/Horse Racing Results.CSV", encoding=result['encoding'])
