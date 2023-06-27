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
