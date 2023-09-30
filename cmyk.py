from PIL import Image
import numpy as np

# 例: 3x3のCMYKデータ
cmyk_data = np.array([
    [[0, 100, 100, 0], [100, 0, 100, 0], [100, 100, 0, 0]],
    [[100, 0, 0, 100], [0, 100, 0, 100], [0, 0, 100, 100]],
    [[0, 0, 0, 0], [100, 100, 100, 100], [50, 50, 50, 50]]
], dtype=np.uint8)

# CMYKデータをPillowのImageオブジェクトに変換
cmyk_image = Image.fromarray(cmyk_data, 'CMYK')

# 画像を表示
cmyk_image.show()
