import cv2
import os

def images_to_mp4(paths, output_path, fps=30):
    # 画像のサイズを取得
    image = cv2.imread(paths[0])
    height, width, _ = image.shape

    # 出力用のMP4ファイルを作成
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # 画像を順番に読み込んでMP4に書き込む
    for path in paths:
        image = cv2.imread(path)
        video_writer.write(image)

    # ファイルを閉じる
    video_writer.release()

# 使用例
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
output_file = "output.mp4"
images_to_mp4(image_paths, output_file)
