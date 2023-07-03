
!yolo mode=track model=yolov8n.pt source={input_video_path} 



!yolo mode=track tracker="botsort.yaml" model=yolov8n.pt conf=0.25 source={input_video_path} save=True 



