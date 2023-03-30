
import zipfile

# ファイル名と保存先ディレクトリを指定する
file_name = 'model.pt'
save_dir = './'

# Zipファイル名を指定する
zip_name = 'submission.zip'

# Zipファイルを作成する
with zipfile.ZipFile(zip_name, mode='w') as zipf:
    zipf.write(file_name, arcname=file_name)
