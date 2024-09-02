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

`ffmpeg`を使ってMKVファイルをMP4に変換し、変換する動画の時間を制限する方法は以下の通りです。

### 基本的なコマンド
以下のコマンドでMKVファイルをMP4に変換し、指定した時間だけのクリップにします。

```bash
ffmpeg -i input.mkv -ss 00:00:00 -t 00:01:00 -c:v libx264 -c:a aac -strict experimental output.mp4
```

### コマンドの詳細
- `-i input.mkv`: 変換元のMKVファイルを指定します。
- `-ss 00:00:00`: 開始時間を設定します（例: 00:00:00 は動画の最初から）。
- `-t 00:01:00`: 変換する時間の長さを指定します（例: 00:01:00 は1分間）。
- `-c:v libx264`: ビデオコーデックとしてH.264を使用します。
- `-c:a aac`: オーディオコーデックとしてAACを使用します。
- `-strict experimental`: AACコーデックの利用に必要なオプション。
- `output.mp4`: 出力ファイル名。

このコマンドでは、`input.mkv`の先頭から1分間だけを切り取って`output.mp4`に変換します。`-ss`と`-t`の値を変更すれば、開始位置と時間長を調整できます。

### その他のオプション
- `-crf 23`: 画質を調整するオプション。値が低いほど画質が高くなり、ファイルサイズも大きくなります。
- `-preset fast`: エンコード速度を調整するオプション。`ultrafast`から`veryslow`まで設定でき、遅いほど品質が良くなります。


