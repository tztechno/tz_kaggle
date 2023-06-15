##############################################

from moviepy.editor import VideoFileClip

def get_fps(mp4_file):
    video = VideoFileClip(mp4_file)
    fps = video.fps
    video.close()
    return fps

mp4_file_path = "path/to/your/video.mp4"
fps = get_fps(mp4_file_path)
print("FPS:", fps)

##############################################

from moviepy.editor import VideoFileClip

def get_mp4_info(filename):
    clip = VideoFileClip(filename)
    duration = clip.duration
    frame_count = clip.reader.nframes
    fps = clip.reader.fps
    clip.close()
    return duration, frame_count, fps

# 使用例
filename = "example.mp4"
duration, frame_count, fps = get_mp4_info(filename)
print("長さ（秒）:", duration)
print("フレーム数:", frame_count)
print("FPS:", fps)

##############################################
