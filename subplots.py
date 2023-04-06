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
