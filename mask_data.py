import cv2
import numpy as np

def color_mask_to_mask_data(color_mask_image, class_colors):
    """
    カラーのMask画像からMaskデータに変換する関数

    Args:
        color_mask_image (numpy.ndarray): カラーのMask画像
        class_colors (list): 各クラスのカラー値（BGR形式）

    Returns:
        mask_data (numpy.ndarray): Maskデータ（各ピクセルのクラスID）
    """
    # 入力画像をBGR形式で読み込む
    mask_image = cv2.imread(color_mask_image)

    # 出力のMaskデータを初期化
    mask_data = np.zeros((mask_image.shape[0], mask_image.shape[1]), dtype=np.uint8)

    # 各クラスのカラー値と対応するクラスIDをマッピング
    color_to_class = {tuple(class_colors[i]): i for i in range(len(class_colors))}

    # 各ピクセルを処理してクラスIDを抽出
    for row in range(mask_image.shape[0]):
        for col in range(mask_image.shape[1]):
            pixel_color = tuple(mask_image[row, col])
            if pixel_color in color_to_class:
                mask_data[row, col] = color_to_class[pixel_color]

    return mask_data

# クラスのカラー値を定義
class_colors = [
    [0, 0, 0],     # クラス0のカラー（黒）
    [255, 0, 0],   # クラス1のカラー（赤）
    [0, 255, 0]    # クラス2のカラー（緑）
]

# カラーのMask画像ファイルを指定してMaskデータに変換
color_mask_image_path = 'color_mask.png'  # 画像ファイルのパス
mask_data = color_mask_to_mask_data(color_mask_image_path, class_colors)

# Maskデータを使用してセグメンテーションタスクを実行
# この段階で得られたmask_dataを使用して、モデルのトレーニングや評価を行うことができます
