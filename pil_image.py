from PIL import Image

image = Image.open(img_path)
image.show()

########################################

from PIL import Image, ImageDraw

image = Image.open("画像ファイルのパス")

draw = ImageDraw.Draw(image)

x1, y1 = 100, 100  # 矩形の左上の座標
x2, y2 = 200, 200  # 矩形の右下の座標

draw.rectangle([(x1, y1), (x2, y2)], outline="red", width=2)
image.show()
