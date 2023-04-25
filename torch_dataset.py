######################################################

import torch
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, index):
        path = self.dataframe.loc[index, 'path']
        label = self.dataframe.loc[index, 'label']
        # ここで画像を読み込んだり、前処理を行ったりする
        # 例えば、PILを使用して画像を読み込む場合は以下のように書けます
        # image = Image.open(path).convert('RGB')
        # または、OpenCVを使用する場合は以下のように書けます
        # image = cv2.imread(path)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # 前処理を適用する場合は、以下のように書けます
        # transform = transforms.Compose([
        #     transforms.Resize((224, 224)),
        #     transforms.ToTensor(),
        #     transforms.Normalize(mean=[0.485, 0.456, 0.406],
        #                          std=[0.229, 0.224, 0.225])
        # ])
        # image = transform(image)
        return image, label

######################################################
#create dataset from df of path/label

import torch
from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self, data_df):
        self.data_df = data_df
    
    def __len__(self):
        return len(self.data_df)
    
    def __getitem__(self, idx):
        path, label = self.data_df.iloc[idx]
        img = Image.open(os.path.join(dir0,path)).convert('RGB')
        img = img.resize((224, 224))
        img = torch.tensor(np.array(img)).permute(2,0,1).float() / 255.0
        
        return img, label
    
######################################################

import torch
from torch.utils.data import Dataset

data = torch.randn(640,3,40,40)
labels = torch.randint(0,3,size=(640,))

class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        sample = {'data': self.data[idx], 'label': self.labels[idx]}
        return sample

# データセットを作成する
dataset = MyDataset(data, labels)

######################################################

def dataset_to_data(dataset):
    dataX = []
    dataY = []
    for x, y in dataset:
        dataX.append(x)
        dataY.append(y)
    return dataX, dataY

######################################################

class ImageDataset(Dataset):
    def __init__(self, path_label, transform=None):
        self.path_label = path_label
        self.transform = transform

    def __len__(self):
        return len(self.path_label)

    def __getitem__(self, idx):
        path, label = self.path_label[idx]
        img = Image.open(path).convert('RGB')

        if self.transform is not None:
            img = self.transform(img)

        return img, label
    
######################################################

from torchvision.datasets import ImageFolder

class ImageDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.dataset = ImageFolder(root=root_dir, transform=transform)

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        img, label = self.dataset[idx]

        return img, label

######################################################
