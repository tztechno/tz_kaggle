from PIL import Image
import numpy as np

# 画像の中で（半分以上が）真っ黒な行と列を削除する関数
def remove_black_borders(image):
    img_array = np.array(image)
    
    # 画像の各行、各列の平均輝度を計算
    row_means = np.mean(img_array, axis=1)
    col_means = np.mean(img_array, axis=0)
    
    # 行の平均輝度がしきい値未満の行を削除
    row_mask = row_means > 0  # しきい値を適切に調整してください
    img_array = img_array[row_mask, :]
    
    # 列の平均輝度がしきい値未満の列を削除
    col_mask = col_means > 0  # しきい値を適切に調整してください
    img_array = img_array[:, col_mask]
    
    # PIL Imageに変換して返す
    processed_image = Image.fromarray(img_array)
    
    return processed_image

# パイプラインにこのカスタムTransform関数を組み込む
transform = transforms.Compose([
    remove_black_borders,  # カスタム関数を追加
    transforms.Resize(224),             # 最短辺を224ピクセルにリサイズ
    transforms.CenterCrop(224),         # 最長辺を224ピクセルに中央クロップ
    transforms.ToTensor(),
])

# これ以降、このtransformを画像に適用することで、真っ黒な行と列を削除して前処理が行われます。
