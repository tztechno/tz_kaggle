from moviepy.editor import *

def convert_webm_to_mp4(webm_file, mp4_file):
    video = VideoFileClip(webm_file)
    video.write_videofile(mp4_file, codec='libx264')
