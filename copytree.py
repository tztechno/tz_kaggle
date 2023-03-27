
import os
import shutil

//method1
if not os.path.exists(path1):
    shutil.copytree(path0, path1)

//mehod2
if os.path.exists(path1):
    shutil.rmtree(path1)
shutil.copytree(path0, path1)
