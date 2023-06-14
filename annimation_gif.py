##############################################

def images_to_mp4(paths, output_path, fps=10):
    image = cv2.imread(paths[0])
    height, width, _ = image.shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for path in paths:
        image = cv2.imread(path)
        video_writer.write(image)

    video_writer.release()

    
images_to_mp4(paths, './sketch.mp4')
path2='./sketch.mp4'

!ffmpeg -y -i sketch.mp4 -vf "fps=10" -loop 1 sketch.gif

from IPython.display import Image
Image(open('./sketch.gif','rb').read())

##############################################
output_file = "detections.gif"
imageio.mimsave(output_file, images, duration=20, loop=0) #repeat animation

from IPython.display import Image
Image(open(output_file, 'rb').read())
#display(Image(filename=output_file, format='png', embed=True))

##############################################
import imageio

output_file = "detections.gif"
imageio.mimsave(output_file, images, duration=20)

from IPython.display import Image
#Image(open(output_file, 'rb').read())
display(Image(filename=output_file, format='png', embed=True))

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

import numpy as np
from PIL import Image
import imageio

path0='/kaggle/input/google-research-identify-contrails-reduce-global-warming/train/1000603527582775543/band_08.npy'
np0=np.load(path0)
np0=np0.reshape(256,256,8)
frames=np.transpose(np0,(2,0,1))

for i, frame in enumerate(frames):
    plt.imsave(f"frame_{i}.png", frame)

images = []
for i in range(8):
    image = Image.open(f"frame_{i}.png")
    images.append(np.array(image))

output_file = "detections.gif"
imageio.mimsave(output_file, images, fps=10)

from IPython.display import Image
Image(open(output_file, 'rb').read())


##############################################
