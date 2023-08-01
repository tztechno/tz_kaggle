
################################################################################
from sklearn.model_selection import train_test_split

trainval_ds = keras.utils.image_dataset_from_directory(
    directory ='/kaggle/input/rock-paper-scissor/rps/rps',
    image_size = (224, 224),
    seed = seed_train_validation,
    color_mode='rgb',
    label_mode = 'categorical',
    batch_size=16,
    shuffle = True)

data_list = list(trainval_ds.as_numpy_iterator())
images = np.concatenate([data[0] for data in data_list])
labels = np.concatenate([data[1] for data in data_list])

train_images, val_images, train_labels, val_labels = train_test_split(images, labels, test_size=0.3, random_state=seed_train_validation)

train_ds = tf.data.Dataset.from_tensor_slices((train_images, train_labels)).batch(16).shuffle(True)
val_ds = tf.data.Dataset.from_tensor_slices((val_images, val_labels)).batch(16)

################################################################################
from sklearn.model_selection import train_test_split

data_list = list(data_ds.as_numpy_iterator())
images = np.concatenate([data[0] for data in data_list])
labels = np.concatenate([data[1] for data in data_list])

# Split data into train and remaining (val + test)
train_images, remaining_images, train_labels, remaining_labels = train_test_split(images, labels, test_size=0.4, random_state=seed_train_validation)

# Split remaining data into validation and test
val_images, test_images, val_labels, test_labels = train_test_split(remaining_images, remaining_labels, test_size=0.5, random_state=seed_train_validation)

train_ds = tf.data.Dataset.from_tensor_slices((train_images, train_labels)).batch(16).shuffle(True)
val_ds = tf.data.Dataset.from_tensor_slices((val_images, val_labels)).batch(16)
test_ds = tf.data.Dataset.from_tensor_slices((test_images, test_labels)).batch(16)

################################################################################

    def setup(self, stage=None):
        dataset = datasets.ImageFolder(root=self.root_dir, transform=self.transform)
        n_data = len(dataset)
        n_train = int(0.6 * n_data)
        n_valid = int(0.2 * n_data)
        n_test = n_data - n_train - n_valid

        train_dataset, val_dataset, test_dataset = torch.utils.data.random_split(dataset, [n_train, n_valid, n_test])

        self.train_dataset = DataLoader(train_dataset, batch_size=self.batch_size, shuffle=True)
        self.val_dataset = DataLoader(val_dataset, batch_size=self.batch_size)
        self.test_dataset = DataLoader(test_dataset, batch_size=self.batch_size)
        
################################################################################
