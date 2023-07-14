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

for path in train_anno_paths[0:2]:
    img_path=path[0:-4]+'.jpg'
    with open(path, 'r') as file:
        text = file.read().strip().split("\n")
    data = [line.split() for line in text]
    df = pd.DataFrame(data)
    display(df)
    img=plt.imread(img_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
#################################
