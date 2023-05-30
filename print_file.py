import subprocess

def print_file(file_path):
    subprocess.Popen(['lp', file_path])

# 使用例
file_path = '/path/to/file.txt'
print_file(file_path)
