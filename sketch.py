import cv2
import matplotlib.pyplot as plt

def show_img(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def create_sketch(path):
    image = cv2.imread(path)
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inv_img = 255 - gray_img
    blurred = cv2.GaussianBlur(inv_img, (21,21), 0)
    inv_blur = 255 - blurred
    sketch = cv2.divide(gray_img, inv_blur, scale=256)
    return sketch

path='/kaggle/input/biggest-genderface-recognition-dataset/faces/woman/woman_1000.jpg'
sketch=create_sketch(path)
image=show_img(path)

plt.imshow(image)
plt.axis('off')
plt.show()

plt.imshow(sketch, cmap='gray')
plt.axis('off')
plt.show()

plt.imshow(cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB))
plt.axis('off')
plt.show()
