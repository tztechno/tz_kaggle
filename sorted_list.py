paths=[]
for dirname, _, filenames in os.walk('/kaggle/input/'):
    for filename in filenames:
        if filename[-4:]=='.jpg':
            pathi=os.path.join(dirname, filename)
            orderi=filename[3:-4].replace('(','').replace(')','').replace(' ','').zfill(3)
            paths+=[[pathi,orderi]]
sorted_paths=sorted(paths, key=lambda x: x[1])
print(sorted_paths)

paths2= [x[0] for x in sorted_paths]
print(paths2)
