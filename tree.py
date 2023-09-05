
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
