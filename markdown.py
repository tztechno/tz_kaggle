from IPython.display import display, Markdown

# Markdownファイルのパスを指定
md_file_path = '/kaggle/input/path/to/your/file.md'

# Markdownファイルの内容を表示
with open(md_file_path, 'r') as file:
    md_content = file.read()
    display(Markdown(md_content))
