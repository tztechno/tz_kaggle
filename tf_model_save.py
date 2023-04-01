#############

import tensorflow as tf

# モデルを定義する
inputs = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(128, activation='relu')(inputs)
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# SavedModel形式でモデルを保存する
tf.saved_model.save(model, 'saved_model/')

#############

import tensorflow as tf

# モデルを定義する
inputs = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(128, activation='relu')(inputs)
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Keras H5形式でモデルを保存する
model.save('model.h5')

#############

import tensorflow as tf

# モデルを定義する
inputs = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(128, activation='relu')(inputs)
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# SavedModel形式でモデルを保存する
tf.saved_model.save(model, 'saved_model/')

# TFLite形式でモデルを保存する
converter = tf.lite.TFLiteConverter.from_saved_model('saved_model/')
tflite_model = converter.convert()
open("model.tflite", "wb").write(tflite_model)


#############

import tensorflow as tf
import tf2onnx

# モデルを定義する
inputs = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(128, activation='relu')(inputs)
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# SavedModel形式でモデルを保存する
tf.saved_model.save(model, 'saved_model/')

# ONNX形式でモデルを保存する
tf2onnx.convert.from_saved_model('saved_model/', output_path='model.onnx')

#############

import pickle

# モデルを定義する
inputs = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(128, activation='relu')(inputs)
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Python Pickle形式でモデルを保存する
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

#############

