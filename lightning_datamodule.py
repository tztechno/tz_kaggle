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
