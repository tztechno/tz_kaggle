from torchvision.utils import make_grid

path0='/kaggle/input/imagenet1k1'
dataset = ImageFolder(path0, transform=transform)
folder_names = dataset.classes

album = []
for folder_name in folder_names[0:20]:
    folder_idx = dataset.class_to_idx[folder_name]
    folder_indices = [i for i, (_, label_idx) in enumerate(dataset.samples) if label_idx == folder_idx]
    random_indices = random.sample(folder_indices, k=6)    
    for idx in random_indices:
        image, _ = dataset[idx]
        album.append(image)

album_grid = make_grid(album, nrow=6)
plt.figure(figsize=(12,12*20))
plt.imshow(album_grid.permute(1,2,0))
plt.axis("off")
plt.show()
