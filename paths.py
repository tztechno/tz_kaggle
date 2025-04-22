
#################################################################  

import os

if not os.path.exists('lighteval'):
    os.makedirs('lighteval')
os.chdir('lighteval')

#################################################################  

paths=[]
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        paths+=[(os.path.join(dirname, filename))]

#################################################################      
        
path_label = []
for dirname, _, filenames in os.walk('/kaggle/input/rockpaperscissors'):
    for filename in filenames:
        if filename[-4:] == '.png':
            path = os.path.join(dirname, filename)
            label = dirname.split('/')[-1]
            path_label += [(path, normal_mapping[label])] 

#################################################################      
