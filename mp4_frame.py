================================================================================

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
    
================================================================================

import cv2
import os
import logging

def video_to_frames(video_file, image_dir='/kaggle/working/frames/', image_file='img_%04d.png'):
    logging.basicConfig(level=logging.INFO)
    
    # Debug: Print the type and value of video_file
    logging.info(f"video_file type: {type(video_file)}, value: {video_file}")
    
    if not isinstance(video_file, str):
        raise TypeError(f"video_file must be a string, not {type(video_file)}")

    if not os.path.exists(video_file):
        raise FileNotFoundError(f"Video file not found: {video_file}")

    os.makedirs(image_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        raise IOError(f"Error opening video file: {video_file}")

    frame_count = 0
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            output_path = os.path.join(image_dir, image_file % frame_count)
            cv2.imwrite(output_path, frame)
            frame_count += 1

    except Exception as e:
        logging.error(f"Error processing video: {str(e)}")
    finally:
        cap.release()

    logging.info(f"Processed {frame_count} frames from {video_file}")
    return frame_count

================================================================================
