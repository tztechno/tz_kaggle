========================================

from PIL import Image

# TIFFファイルのパス
input_path = "input_image.tif"
# 出力PNGファイルのパス
output_path = "output_image.png"

# 画像を開いて変換
with Image.open(input_path) as img:
    img.save(output_path, format="PNG")

print("変換が完了しました:", output_path)

========================================

brew install imagemagick

magick convert input_image.tif output_image.png

========================================
