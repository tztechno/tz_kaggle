#########################################################################

from keras.preprocessing.image import ImageDataGenerator

# ImageDataGeneratorのインスタンスを作成
datagen = ImageDataGenerator(
    rescale=1./255,       # 画素値を0-1にスケーリング
    shear_range=0.2,     # シアリング（ずらし）の範囲
    zoom_range=0.2,      # ズームの範囲
    horizontal_flip=True # 水平方向に反転
)

# 画像が格納されているディレクトリからデータを読み込む
train_generator = datagen.flow_from_directory(
    'path/to/train_directory',
    target_size=(image_height, image_width),  # 画像をリサイズするサイズ
    batch_size=batch_size,
    class_mode='binary'  # 2クラス分類の場合は'binary'、多クラス分類の場合は'categorical'
)

# モデルのトレーニング時にImageDataGeneratorを使ってデータを拡張し、モデルに供給
model.fit_generator(
    train_generator,
    steps_per_epoch=total_train_samples // batch_size,  # 1エポックごとのステップ数
    epochs=num_epochs
)

#########################################################################

datagen = ImageDataGenerator(rescale=1.0/255,
                                  zoom_range=0.2,
                                  shear_range=0.2,
                                  rotation_range=10,
                                  width_shift_range=0.2,
                                  height_shift_range=0.2,
                                  horizontal_flip=True,
                                  fill_mode='nearest')

train_ds = keras.utils.image_dataset_from_directory(
    directory = '/kaggle/input/rock-paper-scissor/rps/rps',
    image_size = (224, 224),
    seed = seed_train_validation,
    color_mode = 'rgb',
    label_mode = 'categorical',
    batch_size = 32,
    shuffle = True)

train_ds = train_ds.map(lambda x, y: (datagen.flow(x, batch_size=32, shuffle=False).next(), y))
train_ds = train_ds.take(limit_train_data)

#########################################################################
