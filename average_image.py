
##############################################################

def average_image(paths):
    first_image = cv2.imread(paths[0])
    height, width, layers = first_image.shape
    total_image = np.zeros((height, width, layers), np.float)
    for path in paths[1:]:
        current_image = cv2.imread(path)
        total_image = cv2.add(total_image, current_image.astype(np.float))
    average_image = total_image / len(paths)
    plt.title('average_image')
    plt.imshow(average_image)
    plt.axis('off')
    plt.show()
    cv2.imwrite(os.path.join(image_folder, "average_image.jpg"), average_image)

average_image(paths)

##############################################################


import cv2
import numpy as np
import os

def average_images(image_folder):
    # 画像が保存されているフォルダから画像のリストを取得
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

    # 画像のサイズを取得
    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = first_image.shape

    # 画像の合計を初期化
    total_image = np.zeros((height, width, layers), np.float)

    # 各画像を合計に追加
    for img in images:
        img_path = os.path.join(image_folder, img)
        current_image = cv2.imread(img_path)
        total_image = cv2.add(total_image, current_image.astype(np.float))

    # 画像の枚数で割って平均を計算
    average_image = total_image / len(images)

    # 平均画像を保存
    cv2.imwrite(os.path.join(image_folder, "average_image.jpg"), average_image)

image_folder = "path/to/your/image/folder"
average_images(image_folder)
