
blank_img=np.zeros(image.shape)
white_img=np.ones(image.shape)*255

plt.imshow(image)
plt.savefig('plot0.png')
plt.show()

plt.imshow(blank_img)
show_anns(masks1)
plt.savefig('plot1b.png')
plt.show()

plt.imshow(white_img)
show_anns(masks1)
plt.savefig('plot1w.png')
plt.show()

plt.imshow(image) 
show_anns(masks1)
plt.savefig('plot2.png')
plt.show()

