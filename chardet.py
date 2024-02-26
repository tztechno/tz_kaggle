!pip install chardet
import chardet

with open(paths[0], 'rb') as f:
    result = chardet.detect(f.read())   
encoding = result['encoding']
print(encoding)
