import cv2
import torch
import torchvision.transforms as T

# Define the normalization values
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

# Create the normalization transform
normalize = T.Normalize(mean=mean, std=std)

# Open the MP4 video file
video_path = 'path/to/your/video.mp4'
video_capture = cv2.VideoCapture(video_path)

# Read and normalize each frame of the video
frames = []
while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        break
    
    # Convert the frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Convert the frame to a PyTorch tensor
    frame_tensor = torch.from_numpy(frame_rgb.transpose((2, 0, 1))).float() / 255.0
    
    # Normalize the frame
    normalized_frame = normalize(frame_tensor)
    
    # Append the normalized frame to the list
    frames.append(normalized_frame)

# Release the video capture object
video_capture.release()

# Convert the list of frames to a PyTorch tensor
normalized_video = torch.stack(frames)

# Print the shape of the normalized video tensor
print(normalized_video.shape)
