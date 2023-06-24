from scipy import ndimage

angle = 244
r_img = ndimage.rotate(img, angle, reshape=False)
print(r_img.shape)

plt.figure(figsize=(6,6))
plt.imshow(r_img)
#plt.axis('off')
plt.show()

r_img[np.where((r_img == [0, 0, 0]).all(axis=2))] = [255, 255, 255]
plt.figure(figsize=(6,6))
plt.imshow(r_img)
#plt.axis('off')
plt.show()
