from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def trim_mp4(input_file, output_file, start_time, end_time):
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

# 使用例
input_file = "input.mp4"
output_file = "output.mp4"
start_time = 5  # トリミング開始時間（秒）
end_time = 10   # トリミング終了時間（秒）

trim_mp4(input_file, output_file, start_time, end_time)
