import os

def search_files(folder_path, search_term):
    results = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if search_term in file_name:
                results.append(os.path.join(root, file_name))
    return results

# 使用例
folder_path = '/path/to/folder'
search_term = 'example'
search_results = search_files(folder_path, search_term)
for result in search_results:
    print(result)
