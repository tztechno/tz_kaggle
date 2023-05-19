import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
rc('animation', html='jshtml')

paths=[]
for dirname, _, filenames in os.walk('/kaggle/working/2D'):
    for filename in filenames:
        if filename[-4:]=='.png':
            paths+=[os.path.join(dirname, filename)]
paths=sorted(paths)
print(paths[0:3])

images=[]
for path in paths:
    images+=[cv2.imread(path)]

    
def create_animation(ims):
    fig=plt.figure(figsize=(6,6))
    plt.axis('off')
    im=plt.imshow(cv2.cvtColor(ims[0],cv2.COLOR_BGR2RGB))
    plt.close()
    
    def animate_func(i):
        im.set_array(cv2.cvtColor(ims[i],cv2.COLOR_BGR2RGB))
        return [im]

    return animation.FuncAnimation(fig, animate_func, frames=len(ims), interval=1000/5)    
