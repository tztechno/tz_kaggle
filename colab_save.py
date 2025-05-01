import shutil
from google.colab import files

# 結果フォルダ名
folder_path = 'results'

# zipファイル名
zip_filename = f'{folder_path}.zip'

# フォルダをzip圧縮
shutil.make_archive(folder_path, 'zip', folder_path)

# zipファイルをダウンロード
files.download(zip_filename)
