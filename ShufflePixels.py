from PIL import Image
import random

class ShufflePixels:
    def __init__(self, prob=0.5):
        self.prob = prob

    def __call__(self, img):
        if random.random() < self.prob:
            img = self.shuffle_pixels(img)
        return img

    def shuffle_pixels(self, img):
        img = img.convert('RGB')
        pixels = list(img.getdata())
        random.shuffle(pixels)
        img.putdata(pixels)
        return img

transform = transforms.Compose([
    transforms.Resize(224*4),
    transforms.CenterCrop(224),
    ShufflePixels(),  # カスタムのピクセルシャッフル変換を追加
    transforms.ToTensor(),
])


