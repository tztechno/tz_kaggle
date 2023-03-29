
import os

# 新しいディレクトリ名を指定
new_folder = "xxx"

# 現在の作業ディレクトリに新しいディレクトリを作成
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
    
