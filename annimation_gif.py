
##############################################

!ffmpeg -y -i detections.mp4 -vf "fps=10" -loop 0 detections.gif

from IPython.display import Image
Image(open('./detections.gif','rb').read())

##############################################

#np.array to gif

import numpy as np
from PIL import Image
import imageio

# 例としてランダムなRGB画像を作成
width, height = 100, 100
num_frames = 10
frames = np.random.randint(0, 255, (num_frames, height, width, 3), dtype=np.uint8)

# 各フレームをPNGとして保存
for i, frame in enumerate(frames):
    image = Image.fromarray(frame)
    image.save(f"frame_{i}.png")

# 保存したフレームからGIFを生成
images = []
for i in range(num_frames):
    image = Image.open(f"frame_{i}.png")
    images.append(np.array(image))

output_file = "detections.gif"
imageio.mimsave(output_file, images, fps=10)

# 生成したGIFを表示
from IPython.display import Image
Image(open(output_file, 'rb').read())

##############################################
