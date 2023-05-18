#############################################

image = cv2.imread(path)
image = cv2.cvtColor(image, CV2.COLOR_BGR2GRY)
image = cv2.resize(image,dsize=(200,200))
    
#############################################    

image0 = cv2.imread(path0)
image0 = cv2.cvtColor(image0, cv2.COLOR_BGR2RGB)
image = cv2.resize(image0,dsize=None,fx=0.1,fy=0.1)

#############################################   
