import requests
import tensorflow as tf

def load_image(img_path):
    response = requests.get(img_path)
    img = tf.image.decode_image(response.content, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img
