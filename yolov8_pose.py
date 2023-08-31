# Build a new model from YAML and start training from scratch
yolo pose train data=coco8-pose.yaml model=yolov8n-pose.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo pose train data=coco8-pose.yaml model=yolov8n-pose.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo pose train data=coco8-pose.yaml model=yolov8n-pose.yaml pretrained=yolov8n-pose.pt epochs=100 imgsz=640

yolo pose val model=yolov8n-pose.pt  # val official model
yolo pose val model=path/to/best.pt  # val custom model

yolo pose predict model=yolov8n-pose.pt source='https://ultralytics.com/images/bus.jpg'  # predict with official model
yolo pose predict model=path/to/best.pt source='https://ultralytics.com/images/bus.jpg'  # predict with custom model

yolo export model=yolov8n-pose.pt format=onnx  # export official model
yolo export model=path/to/best.pt format=onnx  # export custom trained model

