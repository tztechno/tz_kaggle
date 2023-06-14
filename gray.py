########################################################



########################################################
from PIL import Image

def convert_to_gray(image_path):
    # 画像を開く
    image = Image.open(image_path)
    
    # グレースケールに変換
    gray_image = image.convert("L")
    
    # グレースケール画像を保存
    gray_image.save("gray_image.jpg")
    
    print("グレースケール画像を保存しました。")

# 画像のパスを指定して呼び出し
convert_to_gray("input_image.jpg")
########################################################
