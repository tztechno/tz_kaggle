###################################################

    def setup(self, stage=None):
        n_data = len(self.data_df)
        n_train = int(0.8 * n_data)
        n_test = n_data - n_train
        train_dataset, test_dataset = torch.utils.data.random_split(dataset, [n_train, n_test])
        self.train_dataset = DataLoader(train_dataset, batch_size=self.batch_size, shuffle=True)
        self.test_dataset = DataLoader(test_dataset, batch_size=self.batch_size)

###################################################

class DataModule(pl.LightningDataModule):
    
    def __init__(self, transform=transform, batch_size=32):
        super().__init__()
        self.root_dir = "/kaggle/input/four-shapes/shapes"
        self.transform = transform
        self.batch_size = batch_size

    def setup(self, stage=None):
        data = datasets.ImageFolder(root=self.root_dir, transform=self.transform)
        n_data = len(data)
        n_train = n_data*4//5
        
        train_indices = list(range(n_train))
        test_indices = list(range(n_train, n_data))

        train_sampler = SubsetRandomSampler(train_indices)
        test_sampler = SubsetRandomSampler(test_indices)

        self.train_dataset = DataLoader(data, sampler=train_sampler, batch_size=self.batch_size)
        self.test_dataset = DataLoader(data, sampler=test_sampler, batch_size=self.batch_size)

    def train_dataloader(self):
        return self.train_dataset
        
    #val_dataloader necessary
    def val_dataloader(self):
        return self.test_dataset

    def test_dataloader(self):
        return self.test_dataset
    
###################################################    

class DataModule(pl.LightningDataModule):
    
    def __init__(self, transform=transform, batch_size=32):
        super().__init__()
        self.root_dir = "/kaggle/input/avengers-faces-dataset/images/"
        self.transform = transform
        self.batch_size = batch_size

    def setup(self, stage=None):
        train_dataset = datasets.ImageFolder(root=self.root_dir+'train/', transform=self.transform)
        valid_dataset = datasets.ImageFolder(root=self.root_dir+'val/', transform=self.transform)
        test_dataset = datasets.ImageFolder(root=self.root_dir+'test/', transform=self.transform)

        self.train_dataset = DataLoader(train_dataset, batch_size=self.batch_size, shuffle=True)
        self.valid_dataset = DataLoader(valid_dataset, batch_size=self.batch_size)
        self.test_dataset = DataLoader(test_dataset, batch_size=self.batch_size)

    def train_dataloader(self):
        return self.train_dataset
    
    def valid_dataloader(self):
        return self.valid_dataset
    
    def test_dataloader(self):
        return self.test_dataset

    
###################################################   

class DataModule(pl.LightningDataModule):
    
    def __init__(self, transform=transform, batch_size=32):
        super().__init__()
        self.root_dir = "/kaggle/working/datasets"
        self.transform = transform
        self.batch_size = batch_size

    def setup(self, stage=None):
        dataset = datasets.ImageFolder(root=self.root_dir, transform=self.transform)
        n_data = len(dataset)
        n_train = int(0.8 * n_data)
        n_test = n_data - n_train

        train_dataset, test_dataset = torch.utils.data.random_split(dataset, [n_train, n_test])

        self.train_dataset = DataLoader(train_dataset, batch_size=self.batch_size, shuffle=True)
        self.test_dataset = DataLoader(test_dataset, batch_size=self.batch_size)

    def train_dataloader(self):
        return self.train_dataset

    def test_dataloader(self):
        return self.test_dataset

###################################################   

class DataModule(pl.LightningDataModule):
    
    def __init__(self, transform=transform, batch_size=32):
        super().__init__()
        self.root_dir = "datasets"
        self.transform = transform
        self.batch_size = batch_size

    def setup(self, stage=None):
        data = datasets.ImageFolder(root=self.root_dir, transform=self.transform)
        n_data = len(data)
        print(n_data)
        n_train = n_data*3//5
        n_valid = n_data//5

        indices = list(range(n_data))
        random.shuffle(indices)  
        
        train_indices = indices[0:n_train]
        valid_indices = indices[n_train:n_train+n_valid]
        test_indices = indices[n_train+n_valid:]      

        self.train_dataset = DataLoader(Subset(data, train_indices), batch_size=self.batch_size)
        self.valid_dataset = DataLoader(Subset(data, valid_indices), batch_size=self.batch_size)
        self.test_dataset = DataLoader(Subset(data, test_indices), batch_size=self.batch_size)

    def train_dataloader(self):
        return self.train_dataset

    def val_dataloader(self):
        return self.test_dataset

    def test_dataloader(self):
        return self.test_dataset

###################################################   
### in case of no image folder

class ImageDataset(Dataset):
    def __init__(self, path_label, transform=None):
        self.path_label = path_label
        self.transform = transform

    def __len__(self):
        return len(self.path_label)

    def __getitem__(self, idx):
        path, label = self.path_label[idx]
        img = cv2.imread(path) 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)     

        if self.transform is not None:
            img = self.transform(img)

        return img, label

class DataModule(pl.LightningDataModule):
    
    def __init__(self, transform=transform, batch_size=32):
        super().__init__()
        self.root_dir = "/kaggle/input/waveform-images-of-bengali-sound"
        self.transform = transform
        self.batch_size = batch_size

    def setup(self, stage=None):
        dataset = ImageDataset(path_label)
        n_data = len(dataset)
        print(n_data)
        n_train = int(0.5 * n_data)
        n_valid = int(0.2 * n_data)
        n_test = n_data - n_train - n_valid

        train_dataset, val_dataset, test_dataset = torch.utils.data.random_split(dataset, [n_train, n_valid, n_test])

        self.train_dataset = DataLoader(train_dataset, batch_size=self.batch_size, shuffle=True)
        self.val_dataset = DataLoader(val_dataset, batch_size=self.batch_size)
        self.test_dataset = DataLoader(test_dataset, batch_size=self.batch_size)
        
    def train_dataloader(self):
        return self.train_dataset
    
    def val_dataloader(self):
        return self.val_dataset
    
    def test_dataloader(self):
        return self.test_dataset

###################################################   

