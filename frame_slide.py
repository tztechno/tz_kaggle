


def video2frames(video_file=path_mp2, image_dir='/kaggle/working/sample2/', image_file='img_%s.png'):
    i = 0
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        flag, frame = cap.read()
        if flag == False:
            break
        cv2.imwrite(image_dir+image_file % str(i).zfill(5), frame) 
        i += 1
    cap.release()
    
video2frames()

paths0=[]
for dirname, _, filenames in os.walk('/kaggle/working/sample2/'):
    for filename in filenames:
        if filename[-4:]=='.png':
            paths0+=[(os.path.join(dirname, filename))]
paths0=sorted(paths0)            
images0=[]
for i in tqdm(range(len(paths0))):
    images0+=[cv2.imread(paths0[i])]

def create_animation(ims):
    fig=plt.figure(figsize=(12,8))
    im=plt.imshow(cv2.cvtColor(ims[0],cv2.COLOR_BGR2RGB))
    text = plt.text(0.05, 0.05, f'Slide {0}', transform=fig.transFigure, fontsize=14, color='blue')
    plt.axis('off')
    plt.close()

    def animate_func(i):
        im.set_array(cv2.cvtColor(ims[i],cv2.COLOR_BGR2RGB))
        text.set_text(f'Slide {20+i}')        
        return [im]    
    
    return animation.FuncAnimation(fig, animate_func, frames=len(ims), interval=1000//10)

create_animation(np.array(images0)[20:])
