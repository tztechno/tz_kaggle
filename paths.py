paths=[]
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        paths+=[(os.path.join(dirname, filename))]
