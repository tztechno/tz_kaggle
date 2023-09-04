import tensorflow as tf
video_tensor = tf.io.read_file('output.mp4')
tensor = tf.image.decode_video(video_tensor)
