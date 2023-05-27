

!python examples/track.py  --yolo-model yolov8n.pt      # bboxes only
                                        yolov8n-seg.pt  # bboxes + segmentation masks
                                        yolov8n-pose.pt # bboxes + pose estimation

    
!python  examples/track.py  --source sample.mp4  --save  --yolo-model yolov8n.pt    
 
  
## webcam    
!python track.py  --source 0  --yolo-model checkpoints/yolov5s.pt  --reid-model CLIP-RN50


## video
!python track.py  --source VIDEO_PATH  --yolo-model checkpoints/yolov5s.pt  --reid-model CLIP-RN50    
 
  
## track person and car classes
!python track.py  --source 0  --yolo-model checkpoints/yolov5s.pt  --reid-model CLIP-RN50  --filter-class 0 2    
    
    

    
## for each item  
## https://github.com/mikel-brostrom/yolo_tracking

$ python examples/track.py --yolo-model yolov8n.pt      # bboxes only
                                        yolov8n-seg.pt  # bboxes + segmentation masks
                                        yolov8n-pose.pt # bboxes + pose estimation    
    
    
$ python examples/track.py --tracking-method deepocsort  #default
                                             strongsort
                                             ocsort
                                             bytetrack
                                             botsort    
    
$ python examples/track.py --source 0                               # webcam
                                    img.jpg                         # image
                                    vid.mp4                         # video
                                    path/                           # directory
                                    path/*.jpg                      # glob
                                    'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                                    'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream    

$ python examples/track.py --source 0 --yolo-model yolov8n.pt --img 640
                                                   yolov8s.tflite
                                                   yolov8m.pt
                                                   yolov8l.onnx 
                                                   yolov8x.pt --img 1280
         
$ python examples/track.py --source 0 --reid-model mobilenetv2_x1_4_dukemtmcreid.pt
                                                   lmbn_n_cuhk03_d.pt
                                                   osnet_x0_25_market1501.pt
                                                   mobilenetv2_x1_4_msmt17.engine
                                                   resnet50_msmt17.onnx
                                                   osnet_x1_0_msmt17.pt
         
$ python examples/yolo_nas_track.py --source 0                        
            
            


