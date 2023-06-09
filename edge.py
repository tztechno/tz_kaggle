#################################################

image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
smooth = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(smooth, 50, 150) 
edges = cv2.bitwise_not(edges)
image=cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)

#################################################

def edge(path):
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    smooth = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(smooth, 50, 150) 
    edges = cv2.bitwise_not(edges)
    image=cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)
    return image
  
#################################################
