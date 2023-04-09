class NumpyDataset(Dataset):
    def __init__(self, X, Y, transform=None):
        self.X = X
        self.Y = Y
        self.transform = transform

    def __len__(self):
        return len(self.X)

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def set_transform(self, transform):
        self.transform = transform

    def __getitem__(self, index):
        x = self.X[index]
        y = self.Y[index]
        if self.transform is not None:
            x = self.transform(x)
        x = torch.from_numpy(x.astype(int))
        y = np.array(y, dtype=np.ndarray)  
        y = torch.from_numpy(y.astype(int))
        return x, y
