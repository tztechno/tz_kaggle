
###############################################################

colors13=[(128,128,0),
(255,255,0),
(255,0,255),
(192,192,192),
(0,255,255),
(0,255,0),
(255,0,0),
(0,0,255),
(0,128,0),
(128,0,128),
(0,0,128),
(0,128,128),
(128,0,0)]

###############################################################

for i,path in enumerate(paths):
    order=path.split('/')[-1][4:7]
    #print(order)
    img = cv2.imread(path)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    H,W=img.shape[0],img.shape[1]
    
    orderint=int(order)
    for k in range(orderint):
        datai=data0[data0['order']==str(k).zfill(3)]
        for j in range(len(datai)):
            c=colors13[int(datai.iloc[j,5])%13]
            x,y=datai.iloc[j,1],datai.iloc[j,2]
            cv2.circle(img,(int(x*W),int(y*H)),3,(c),-1) #(img, center, radius, color, thickness)    
    
    #img=cv2.resize(img,dsize=None,fx=0.3,fy=0.3)
    
    cv2.imwrite('/kaggle/working/frame2/'+order+'.png',img) 
    #print(order)
    #plt.imshow(img)
    #plt.show()


###############################################################

for i,path in enumerate(paths):
    order=path.split('/')[-1][4:7]
    #print(order)
    img = cv2.imread(path)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    H,W=img.shape[0],img.shape[1]
    
    orderint=int(order)
    datai=data0[data0['order']==order]
    dataiB1=data0[data0['order']==str(orderint-3).zfill(3)]   
    dataiB2=data0[data0['order']==str(orderint-6).zfill(3)] 
    dataiB3=data0[data0['order']==str(orderint-9).zfill(3)] 
    dataiB4=data0[data0['order']==str(orderint-12).zfill(3)]  
    
    for j in range(len(datai)):
        c=colors13[int(datai.iloc[j,5])%13]
        x,y=datai.iloc[j,1],datai.iloc[j,2]
        cv2.circle(img,(int(x*W),int(y*H)),8,(c),-1) #(img, center, radius, color, thickness)
    for j in range(len(dataiB1)):
        c=colors13[int(dataiB1.iloc[j,5])%13]
        x,y=dataiB1.iloc[j,1],dataiB1.iloc[j,2]
        cv2.circle(img,(int(x*W),int(y*H)),6,(c),-1) #(img, center, radius, color, thickness)
    for j in range(len(dataiB2)):
        c=colors13[int(dataiB2.iloc[j,5])%13]
        x,y=dataiB2.iloc[j,1],dataiB2.iloc[j,2]
        cv2.circle(img,(int(x*W),int(y*H)),5,(c),-1) #(img, center, radius, color, thickness)
    for j in range(len(dataiB3)):
        c=colors13[int(dataiB3.iloc[j,5])%13]
        x,y=dataiB3.iloc[j,1],dataiB3.iloc[j,2]
        cv2.circle(img,(int(x*W),int(y*H)),4,(c),-1) #(img, center, radius, color, thickness)
    for j in range(len(dataiB4)):
        c=colors13[int(dataiB4.iloc[j,5])%13]
        x,y=dataiB4.iloc[j,1],dataiB4.iloc[j,2]
        cv2.circle(img,(int(x*W),int(y*H)),3,(c),-1) #(img, center, radius, color, thickness)    
        
    #img=cv2.resize(img,dsize=None,fx=0.3,fy=0.3)
    
    cv2.imwrite('/kaggle/working/frame2/'+order+'.png',img) 
    #print(order)
    #plt.imshow(img)
    #plt.show()

###############################################################
