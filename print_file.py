import os

def print_file_names_in_folder(folder_path):
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        print(file_name)

# 使用例
folder_path = '/path/to/folder'
print_file_names_in_folder(folder_path)
