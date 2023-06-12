import torch
import torchvision
import matplotlib.pyplot as plt

# 画像を読み込む
image_path = 'save.png'
image = torchvision.io.read_image(image_path)
image_np = image.permute(1,2,0).numpy()  # (C, H, W) -> (H, W, C)

# 画像を表示
plt.imshow(image_np)
plt.axis('off')
plt.show()
