
ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

import os
import shutil
from google.colab import files

folder_path = "data"
zip_filename = "data.zip"

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    shutil.make_archive(folder_path, 'zip', folder_path)
    files.download(zip_filename)
else:
    print(f"フォルダ '{folder_path}' が存在しません。")

ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
