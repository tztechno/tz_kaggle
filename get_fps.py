from moviepy.editor import VideoFileClip

def get_fps(mp4_file):
    video = VideoFileClip(mp4_file)
    fps = video.fps
    video.close()
    return fps

mp4_file_path = "path/to/your/video.mp4"
fps = get_fps(mp4_file_path)
print("FPS:", fps)
