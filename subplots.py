######################################

indices = np.random.choice(trainX.shape[0], 9)
fig, axs = plt.subplots(3, 3, figsize=(8,8))
for i, ax in enumerate(axs.flatten()):
    ax.imshow(trainX[indices[i]].transpose(1,2,0))
    ax.axis("off")
    ax.set_title(normal_mapping[trainY[indices[i]]])
plt.tight_layout()
plt.show()

######################################

from PIL import Image
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
for i, ax in enumerate(axes.ravel()):
    if i < len(indices):
        image = Image.fromarray(trainX[indices[i]])
        ax.imshow(image)
        ax.axis('off')
        ax.set_title(normal_mapping[trainY[indices[i]]])
plt.show()

######################################

indices = random.sample(range(len(paths2)),16)
fig, axs = plt.subplots(4, 4, figsize=(8,8))
for i, ax in enumerate(axs.flatten()):
    path=paths2[indices[i]]
    #print(path)
    img=cv2.imread(path)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    ax.imshow(img)
    ax.axis("off")
plt.tight_layout()
plt.show()

######################################

fig, axs = plt.subplots(3,3,figsize=(9,9))
for i in range(9):
    r=i//3
    c=i%3
    img1 = cv2.imread(filesA2[i])
    file=filesA2[i].split('/')[-1][0:-4]
    ax=axs[r][c].axis("off")
    ax=axs[r][c].set_title(file)
    ax=axs[r][c].imshow(img1)
plt.show()

######################################

for images, labels in dataloader:
    break
fig, axs = plt.subplots(16,4, figsize=(12,48))
for i, ax in enumerate(axs.flatten()):
    img=np.transpose(images[i].numpy(),(1,2,0))
    ax.set_title(reverse_mapping[int(labels[i])])
    ax.imshow(img)
    ax.axis("off")
plt.tight_layout()
plt.show()

######################################

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

######################################

random_idx = np.random.randint(1, len(path_label), size=9)
fig, axes = plt.subplots(3,3, figsize=(10,10))

for idx, ax in enumerate(axes.ravel()):
    img = Image.open(path_label[idx][0])
    label=path_label[idx][1]
    ax.set_title(reverse_mapping[label])
    ax.axis('off')
    ax.imshow(img)
    
######################################
