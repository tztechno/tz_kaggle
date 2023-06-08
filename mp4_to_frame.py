
import cv2

def video_2_frames(video_file=paths[0], image_dir='/kaggle/working/frame/', image_file='img_%s.png'):
    i = 0
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        flag, frame = cap.read()
        if flag == False:
            break
        cv2.imwrite(image_dir+image_file % str(i).zfill(4), frame) 
        i += 1
    cap.release()
