from moviepy.editor import VideoFileClip
video = VideoFileClip(path)
frame_rate = video.fps
print(frame_rate)
