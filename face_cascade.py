
import random
import cv2
import matplotlib.pyplot as plt

path_cas='/kaggle/input/haar-cascades-for-face-detection/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(path_cas)

for i,path in enumerate(random.sample(frame_paths,5)):   
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    try:
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        lenf=len(faces)
        if lenf>0:
            print(lenf)
            f, ax = plt.subplots(1,1+lenf, figsize=(2*(1+lenf),2))
            ax[0].imshow(img, aspect='auto') 
            ax[0].set_xticks([]) 
            ax[0].set_yticks([])            
            for j,(x,y,w,h) in enumerate(faces):
                #print(x,y,w,h)
                face = img[y:y+h, x:x+w]
                face_file = str(i).zfill(4)+'_'+str(j).zfill(2)+'.png'
                face_path = os.path.join(d_faces,face_file)
                ax[j+1].imshow(face, aspect='auto')
                ax[j+1].set_xticks([]) 
                ax[j+1].set_yticks([])
                cv2.imwrite(face_path, cv2.cvtColor(face, cv2.COLOR_BGR2RGB))                
            plt.show()
    except:
        print('except')
        continue
