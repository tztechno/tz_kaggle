https://www.kaggle.com/code/stpeteishii/clip-fire-area-from-video

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
rc('animation', html='jshtml')
from IPython.display import Image, Video
from matplotlib.animation import FuncAnimation

* imageR: RGB image
* imageB: BGR image

path_mp4='/kaggle/input/forest-fire-dataset-video/Forest fire dataset video/Dataset/Fire.mp4'

# movie to frame

!mkdir frame

def video_2_frames(video_file=path_mp4, image_dir='/kaggle/working/frame/', image_file='img_%s.png'):
    i = 0
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        flag, frame = cap.read()
        if flag == False:
            break
        cv2.imwrite(image_dir+image_file % str(i).zfill(4), frame) 
        i += 1
    cap.release()

video_2_frames()

path0='/kaggle/working/frame/img_0095.png'
imageB = cv2.imread(path0)#BGR
imageR=cv2.cvtColor(imageB, cv2.COLOR_BGR2RGB)

image1 = cv2.cvtColor(imageB[113:117,191:195], cv2.COLOR_BGR2RGB)
cv2.rectangle(imageR,(191,113),(195,117), (255, 0, 0) ,1)
plt.figure(figsize=(10,4))
plt.imshow(imageR)
#plt.axis('off')
plt.show()

image_list = [image1]

concatenated_image = np.concatenate(image_list, axis=1)
plt.figure(figsize=(10, 2))
plt.imshow(concatenated_image)
plt.axis('off')
plt.show()

def judge_mean_color(image):
    mean_red = np.mean(image[:,:,0])  
    mean_green = np.mean(image[:,:,1])  
    mean_blue = np.mean(image[:,:,2]) 
    
    min_red = np.min(image[:,:,0])  
    min_green = np.min(image[:,:,1])  
    min_blue = np.min(image[:,:,2])   
    
    max_red = np.max(image[:,:,0])  
    max_green = np.max(image[:,:,1])  
    max_blue = np.max(image[:,:,2])     
    
    nc=[ np.array((int(round(mean_red,0)),int(round(mean_green,0)),int(round(mean_blue,0)))) ]
    min_nc=[ np.array((int(round(min_red,0)),int(round(min_green,0)),int(round(min_blue,0)))) ]
    max_nc=[ np.array((int(round(max_red,0)),int(round(max_green,0)),int(round(max_blue,0)))) ]
    
    print('mean',tuple(nc[0]),', min',tuple(min_nc[0]),', max',tuple(max_nc[0]))
   
    image_list = [[nc],[min_nc],[max_nc]]

    concatenated_image = np.concatenate(image_list, axis=1)
    plt.figure(figsize=(10, 2))
    plt.imshow(concatenated_image)
    plt.axis('off')
    plt.show()
    return min_nc,max_nc
    
min_nc,max_nc=judge_mean_color(concatenated_image)   

lower_color = np.array(min_nc[0])  # lower RGB value
upper_color = np.array(max_nc[0])  # upper RGB value

# RGB variation
color_variations = np.linspace(lower_color, upper_color, 100)

fig, ax = plt.subplots(figsize=(10,5))
ax.imshow([color_variations.astype(int)])
ax.axis('off')
plt.show()

imageR=cv2.cvtColor(imageB, cv2.COLOR_BGR2RGB)
mask = (imageR >= lower_color) & (imageR <= upper_color)
mask = mask.all(axis=-1) 
cropped_image = imageR.copy()
#cropped_image[mask] = [255,255,255]  # non-mask region to white
cropped_image[~mask] = [0,0,0]  # mask region to black

def change_image(path):
    imageB=cv2.imread(path)
    imageR=cv2.cvtColor(imageB, cv2.COLOR_BGR2RGB)    
    mask = (imageR >= lower_color) & (imageR <= upper_color)
    mask = mask.all(axis=-1) 
    cropped_image = imageR.copy()
    #cropped_image[mask] = [255,255,255]  # non-mask region to white
    cropped_image[~mask] = [0,0,0]  # mask region to black 
    return cropped_image

plt.imshow(imageR)
plt.show()
plt.imshow(cropped_image)
plt.show()

paths=[]
for dirname, _, filenames in os.walk('frame'):
    for filename in filenames:
        paths+=[(os.path.join(dirname, filename))]
paths.sort()

images = []
for path in paths:
    image=plt.imread(path)
    images+=[image]

def update(frame):
    plt.clf()
    plt.imshow(images[frame])
    plt.axis('off')

ani = FuncAnimation(plt.gcf(), update, frames=len(images), interval=300)
ani.save('original.gif', writer='pillow', fps=30)

Image(open('./original.gif','rb').read())

fimages = []
for path in paths:
    image=change_image(path)
    fimages+=[image]

def update2(frame):
    plt.clf()
    plt.imshow(fimages[frame])
    plt.axis('off')

ani = FuncAnimation(plt.gcf(), update2, frames=len(fimages), interval=300)
ani.save('fire.gif', writer='pillow', fps=30)

Image(open('./fire.gif','rb').read())
