#####################################################

import tensorflow as tf
from tensorflow import keras

data_ds = keras.utils.image_dataset_from_directory(
    directory ='/kaggle/input/biggest-genderface-recognition-dataset/faces',
    image_size = (224, 224),
    seed = seed_train_validation,
    color_mode='rgb',
    label_mode = 'categorical',
    batch_size=32,
    shuffle = True)

data_list = list(data_ds.as_numpy_iterator())
images = np.concatenate([data[0] for data in data_list])
labels = np.concatenate([data[1] for data in data_list])

train_images,testval_images,train_labels,testval_labels = train_test_split(
    images, labels, test_size=0.3, random_state=seed_train_validation)

test_images,val_images,test_labels,val_labels = train_test_split(
    testval_images, testval_labels, test_size=0.5, random_state=seed_train_validation)

train_ds = tf.data.Dataset.from_tensor_slices((train_images, train_labels)).batch(16).shuffle(True)
val_ds = tf.data.Dataset.from_tensor_slices((val_images, val_labels)).batch(16)
test_ds = tf.data.Dataset.from_tensor_slices((test_images, test_labels)).batch(16)

#####################################################

val_dataset, test_dataset = torch.utils.data.random_split(valtestset, [n_val, n_test])

#####################################################
