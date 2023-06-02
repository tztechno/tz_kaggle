os.makedirs('datasets', exist_ok=True)
os.makedirs('datasets/train', exist_ok=True)
os.makedirs('datasets/valid', exist_ok=True)
os.makedirs('datasets/test', exist_ok=True)
os.makedirs('datasets/train/images', exist_ok=True)
os.makedirs('datasets/valid/images', exist_ok=True)
os.makedirs('datasets/test/images', exist_ok=True)
os.makedirs('datasets/train/labels', exist_ok=True)
os.makedirs('datasets/valid/labels', exist_ok=True)
os.makedirs('datasets/test/labels', exist_ok=True)

for path in paths:
    file=path.split('/')[-1]
    txjpg=file[-4:]
    imlab=path.split('/')[-2]
    tt=path.split('/')[-3]
    !cp /kaggle/input/taco-data-downsized-for-yolo-nas/datasets/{tt}/{imlab}/{file}  /kaggle/working/datasets/{tt}/{imlab}/{file}

!ls datasets/train/images
