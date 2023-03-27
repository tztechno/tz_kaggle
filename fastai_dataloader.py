#fastai dls



#########################################

from fastai.vision.all import *

# 画像ファイルのパスを取得するための正規表現
path = Path("path/to/images")
pat = r'(\w+)_\d+.png$'

# データブロックを定義する
dblock = DataBlock(
    blocks=(ImageBlock, CategoryBlock),  # 入力データの種類を定義
    get_items=get_image_files,  # 画像ファイルを取得する関数を定義
    splitter=RandomSplitter(),  # 訓練用と検証用のデータをランダムに分割する
    get_y=using_attr(RegexLabeller(pat), 'name'),  # ラベルをファイル名から抽出する
    item_tfms=Resize(256),  # 画像のサイズをリサイズする
    batch_tfms=aug_transforms()  # ミニバッチに対して行うデータ拡張の方法を定義
)

# データローダーを作成する
dls = dblock.dataloaders(path, bs=16)


#########################################

dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192, method='squish')]
).dataloaders(path, bs=32)

dls.show_batch(max_n=6)

#########################################

