import subprocess

def print_files_in_folder(folder_path):
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        subprocess.Popen(['lp', file_path])

# 使用例
folder_path = '/path/to/folder'
print_files_in_folder(folder_path)
