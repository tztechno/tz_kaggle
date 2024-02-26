
##########################

import json

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            json_data = json.loads(line)
            data.append(json_data)
    return data

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

# Load the data
file_path = '/kaggle/input/synthetic-student-profiles-dataset/student_profiles.jsonl'
data = []
with open(file_path, 'r') as file:
    for line in file:
        data.append(json.loads(line))
df = pd.DataFrame(data)

##########################
