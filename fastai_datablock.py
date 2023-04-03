
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

