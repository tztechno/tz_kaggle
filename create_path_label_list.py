import pandas as pd

def create_path_label_list(df):
    path_label_list = []
    for _, row in df.iterrows():
        path = row['path']
        label = row['label']
        path_label_list.append((path, label))
    return path_label_list

# サンプルのDataFrame
df = pd.DataFrame({
    'path': ['path1', 'path2', 'path3'],
    'label': ['label1', 'label2', 'label3']
})

# path_labelのリストを作成
path_label_list = create_path_label_list(df)
print(path_label_list)
