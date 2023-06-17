import os

def delete_files_with_extension(folder_path, extension):
    # 指定したフォルダ内のすべてのファイルを取得
    files = os.listdir(folder_path)

    # 指定した拡張子のファイルを削除
    for file in files:
        if file.endswith(extension):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# 使用例
folder_path = "/path/to/folder"  # フォルダのパスを指定
extension = ".txt"  # 削除したいファイルの拡張子を指定

delete_files_with_extension(folder_path, extension)
