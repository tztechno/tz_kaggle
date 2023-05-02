####################

    def __getitem__(self, idx):
        label = self.label[idx]        
        img_path = self.path[idx]
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.resize(img,dsize=(224,224))
        img = torch.from_numpy(np.transpose(img,(2,0,1)))
        #print(type(img),img.dtype,type(label),label.dtype)
        return img, label

####################
