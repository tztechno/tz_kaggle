
##################################################

import lighteval
import inspect

def print_module_tree(module, indent=0):
    prefix = " " * indent
    print(f"{prefix}{module.__name__.split('.')[-1]}/")
    members = inspect.getmembers(module)
    for name, member in members:
        if inspect.ismodule(member) and member.__name__.startswith(module.__name__):
            print_module_tree(member, indent + 4)
        elif inspect.isfunction(member) or inspect.isclass(member):
            print(f"{' ' * (indent + 4)}{name}")

print_module_tree(lighteval)

##################################################



import os

def print_directory_tree(start_path, prefix=""):
    items = os.listdir(start_path)
    items.sort()  # アルファベット順にソート
    for index, item in enumerate(items):
        path = os.path.join(start_path, item)
        connector = "└── " if index == len(items) - 1 else "├── "
        print(prefix + connector + item)
        if os.path.isdir(path):
            extension = "    " if index == len(items) - 1 else "│   "
            print_directory_tree(path, prefix + extension)

# 使用例：現在のフォルダを表示
print_directory_tree(".")


##################################################

import os

def tree(directory, level=0):
    prefix = "|   " * level
    prefix += "|-- "    
    contents = os.listdir(directory)    
    for item in sorted(contents):
        item_path = os.path.join(directory, item)        
        if os.path.isdir(item_path):
            print(prefix + item + "/")
            tree(item_path, level+1)
        else:
            print(prefix + item)

# フォルダのパスを指定して実行する
folder_path = "/path/to/folder"
tree(folder_path)

##################################################

!tree -I *.npz /kaggle/input/predict-ai-model-runtime/

##################################################
