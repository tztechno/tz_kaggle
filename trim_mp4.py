from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def trim_video(input_file, output_file, start_time, end_time):
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)
