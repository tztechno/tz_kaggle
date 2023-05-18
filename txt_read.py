#################################

file_path = "path/to/file.txt"

with open(file_path, 'r') as file:
    content = file.read()

print(content)

#################################

from pathlib import Path

file_path = Path("path/to/file.txt")

with file_path.open('r') as file:
    content = file.read()

print(content)

#################################
