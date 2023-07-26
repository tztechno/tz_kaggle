limit_train_data = 500
limit_val_data = 300

train_datagen = ImageDataGenerator(rescale=1.0/255,
                                  zoom_range=0.2,
                                  shear_range=0.2,
                                  rotation_range=10,
                                  width_shift_range=0.2,
                                  height_shift_range=0.2,
                                  horizontal_flip=True,
                                  fill_mode='nearest')

train_ds = keras.utils.image_dataset_from_directory(
    directory ='/kaggle/input/sports-classification/train',
    image_size = (224, 224),
    seed = seed_train_validation,
    color_mode='rgb',
    label_mode = 'categorical',
    batch_size=32,
    shuffle = shuffle_value).take(limit_train_data) 

val_datagen = ImageDataGenerator(rescale=1.0/255)

val_ds = keras.utils.image_dataset_from_directory(
    directory ='/kaggle/input/sports-classification/valid',
    image_size = (224, 224),
    seed = seed_train_validation,
    label_mode = 'categorical',
    batch_size=32,
    color_mode = 'rgb',
    shuffle = shuffle_value).take(limit_train_data) 

print(len(train_ds),len(val_ds))
