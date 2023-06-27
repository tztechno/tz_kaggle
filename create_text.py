content = '''
This is line 1.
This is line 2.
This is line 3.
'''

file_path = 'example.txt'

with open(file_path, 'w') as file:
    file.write(content)

print(f"テキストファイル '{file_path}' が生成されました。")
