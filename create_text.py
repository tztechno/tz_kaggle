######################################################

content = '''
loguru>=0.7.0
PyYAML>=5.3.1                  
gdown>=4.7.1            
GitPython>=3.1.0        
filterpy>=1.4.5         
'''
file_path = 'requirements.txt'
with open(file_path, 'w') as file:
    file.write(content)

######################################################

content = '''
This is line 1.
This is line 2.
This is line 3.
'''
file_path = 'example.txt'
with open(file_path, 'w') as file:
    file.write(content)

######################################################

def write_list_to_file(lst, filename):
    # ファイルを書き込みモードで開く
    with open(filename, 'w') as file:
        # リストの要素をスペース区切りで書き込む
        file.write(' '.join(str(item) for item in lst))

# テスト用のリスト
my_list = [1, 2, 3, 4, 5]

# ファイル名として使用する文字列
file_name = "output.txt"

# リストをファイルに書き込む
write_list_to_file(my_list, file_name)

######################################################
