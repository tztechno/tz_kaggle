###############################################

import tensorflow as tf
video_tensor = tf.io.read_file('output.mp4')
tensor = tf.image.decode_video(video_tensor)

###############################################

import ffmpeg
video_stream = ffmpeg.input('my_video.mp4')
frame_tensors = [ffmpeg.frame_to_tensor(frame) for frame in video_stream.frames]
print(frame_tensors)

###############################################
