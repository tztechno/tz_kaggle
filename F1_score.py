import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Activation,Dropout,Conv2D, MaxPooling2D,BatchNormalization
from tensorflow.keras.optimizers import Adam, Adamax
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras import regularizers
from tensorflow.keras.models import Model
from tensorflow.keras import backend as K

def F1_score(y_true, y_pred):
    true_positives = K.sum(K.cast(K.equal(y_true, y_pred), dtype='float32'))
    possible_positives = K.sum(K.cast(K.equal(y_true, 1), dtype='float32'))
    predicted_positives = K.sum(K.cast(K.equal(y_pred, 1), dtype='float32'))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2 * (precision * recall) / (precision + recall + K.epsilon())
    return f1_val

f1_score = F1_score(y_true, y_pred)
print("F1 score:", K.eval(f1_score))
