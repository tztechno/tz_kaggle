def make_sketch(path):

    image = cv2.imread(path)
    image2=cv2.resize(image,dsize=None,fx=1.6,fy=1.6)
    gray_img = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_img, threshold1=70, threshold2=100)
    inv_edges = 255 - edges
    
    fig, axs = plt.subplots(1,2,figsize=(14,6))
    ax=axs[0].imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
    ax=axs[1].imshow(cv2.cvtColor(inv_edges, cv2.COLOR_BGR2RGB))
    plt.show()
