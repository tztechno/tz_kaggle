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
