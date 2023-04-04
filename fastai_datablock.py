
####################################################

from fastai.vision.all import *

# NumPy配列からデータを読み込み、データセットを作成する
np_data = np.load('data.npy')
dls = DataBlock(blocks=(ImageBlock, CategoryBlock),
                get_items=get_image_files,
                splitter=RandomSplitter(),
                get_y=parent_label,
                item_tfms=Resize(460),
                batch_tfms=aug_transforms(size=224))

dls = dls.dataloaders(np_data)

####################################################

from fastai.vision.all import *

# 2次元numpy配列の準備
x = np.random.rand(100, 100)
y = np.random.randint(0, 2, size=(100, 100))

# データセットの作成
db = DataBlock(blocks=(ImageBlock(cls=PILImageBW), CategoryBlock),
               get_items=get_image_files,
               splitter=RandomSplitter(),
               get_y=lambda o: y,
               item_tfms=[Resize(224, method='pad', pad_mode='zeros')],
               batch_tfms=[*aug_transforms()])

dls = db.dataloaders(x, bs=32)


####################################################
