def create_edge(path):
    image = cv2.imread(path)
    image = cv2.resize(image,dsize=(500,500))#####
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    smooth = cv2.GaussianBlur(gray, (1,1), 0)
    edges = cv2.Canny(smooth, 10,60) 
    edges = cv2.bitwise_not(edges)
    #edges = cv2.resize(edges,dsize=None,fx=0.5,fy=0.5)#####
    #edges=cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)
    return edges

image =create_edge(path0)
image = np.expand_dims(image0, axis=-1) 
image = np.tile(image,(1,1,3))
plt.axis("off")
plt.imshow(image)
plt.show()

image =cvs.imread(path0)
image =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.axis("off")
plt.imshow(image0)
plt.show()
