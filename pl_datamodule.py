#################################################################

# define the datamodule class
class IrisDataModule(pl.LightningDataModule):
    def __init__(self, data):
        super().__init__()
        self.dataset = IrisDataSet(data)
        
    def setup(self, stage=None):
        if stage == 'fit' or stage is None:
            self.train_data, self.val_data = train_test_split(self.dataset, test_size=0.3, random_state=42)
        
        if stage == 'test' or stage is None:
            self.test_data = self.dataset

    def train_dataloader(self):
        return DataLoader(self.train_data, batch_size=32, shuffle=True, num_workers=2)

    def val_dataloader(self):
        return DataLoader(self.val_data, batch_size=32, num_workers=2)

    def test_dataloader(self):
        return DataLoader(self.test_data, batch_size=32, num_workers=2)

#################################################################
      
class DataModule(pl.LightningDataModule):
    
    def __init__(self, transform=transform, batch_size=32):
        super().__init__()
        self.root_dir = "/kaggle/input/chessman-image-dataset/Chessman-image-dataset/Chess/"
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

#################################################################
