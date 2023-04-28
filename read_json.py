
##########################

import pandas as pd
import json

with open('/kaggle/input/news-category-dataset/News_Category_Dataset_v3.json', 'r') as f:
    data = f.read()

data = [json.loads(line) for line in data.split('\n') if line]
df = pd.DataFrame.from_records(data)

##########################

import json

json_file_path = 'path/to/json/file.json'

with open(json_file_path, 'r') as f:
    data = json.load(f)

##########################

import pandas as pd

# JSONファイルを読み込む
with open('example.json', 'r') as f:
    data = f.read()

# JSONデータをDataFrameに変換する
df = pd.read_json(data)

# DataFrameを表示する
print(df)

##########################

import pandas as pd

# JSONデータを読み込む
url = 'https://example.com/data.json'
data = pd.read_json(url)

# DataFrameを表示する
print(data)

##########################
