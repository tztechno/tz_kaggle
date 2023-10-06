####################################################################

!ffmpeg -y -i detections.mp4 -vf "fps=10" -loop 0 detections.gif
from IPython.display import Image
Image(open('./detections.gif','rb').read())

####################################################################

# animation.gif to mp4
import imageio_ffmpeg as ffmpeg
import imageio

# 入力と出力ファイルのパスを指定
input_gif_path = 'input.gif'
output_mp4_path = 'output.mp4'

# GIFファイルを読み込み、MP4に変換
with imageio.get_reader(input_gif_path) as reader:
    fps = reader.get_meta_data()['fps']  # GIFのフレームレートを取得
    writer = imageio.get_writer(output_mp4_path, fps=fps)
    for frame in reader:
        writer.append_data(frame)
    writer.close()

print(f'{input_gif_path} を {output_mp4_path} に変換しました。')


####################################################################
