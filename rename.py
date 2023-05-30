import os

folder_path = "/path/to/folder"  # フォルダのパスを指定してください

# フォルダ内のファイル名を取得して処理する
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # ファイル名が15文字以上の場合は縮める
    if len(filename) > 15:
        new_filename = filename[-15:]  # 後ろ15文字を抽出
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)
        print(f"{filename} を {new_filename} に変更しました。")
    else:
        print(f"{filename} は縮める必要がありません。")
