######################################################################################
import subprocess

def trim_video(input_file, output_file, start_time, end_time):
    command = ['ffmpeg', '-i', input_file, '-ss', str(start_time), '-to', str(end_time), '-c', 'copy', output_file]
    subprocess.run(command)

input_file = '/kaggle/input/road-traffic-video-monitoring/traffic_video.avi'
output_file = '/kaggle/working/yolov8_tracking/sample.mp4'
start_time = 3
end_time = 18

trim_video(input_file, output_file, start_time, end_time)

######################################################################################

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def trim_video(input_file, output_file, start_time, end_time):
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

######################################################################################
