!pip install moviepy

from moviepy.editor import VideoFileClip, AudioFileClip

# 1. mp4ファイルから音声トラックを抽出
video_clip = VideoFileClip("input.mp4")
audio_clip = video_clip.audio

# 2. 音声トラックを加工（例：音量を2倍にする）
# ここで、audio_clipを加工するコードを記述してください
# 例えば、audio_clip = audio_clip.volumex(2.0) のように音量を2倍にできます

# 3. 新しいmp4ファイルに音声トラックを結合
final_video = video_clip.set_audio(audio_clip)
final_video.write_videofile("output.mp4", codec="libx264")

# 4. 不要な一時ファイルの削除（任意）
# audio_clip.close()
# video_clip.close()
