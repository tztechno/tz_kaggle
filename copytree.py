######################

cp /path/to/source/ /path/to/destination/directory/

######################

import os
import shutil


#method1
if not os.path.exists(path1):
    shutil.copytree(path0, path1)

    
#mehod2
if os.path.exists(path1):
    shutil.rmtree(path1)
shutil.copytree(path0, path1)


#method3
destination = "frame" 
if not os.path.exists(destination):
    os.makedirs(destination)

for filename in os.listdir(path0):
    src_path = os.path.join(path0, filename) 
    if filename.endswith(".jpg"):
        dst_path = os.path.join(destination, filename) 
        shutil.copyfile(src_path, dst_path)  
        
        
