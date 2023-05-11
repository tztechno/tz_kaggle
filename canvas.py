
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

# FigureCanvasを作成し、レンダリングする
canvas = fig.canvas
canvas.draw()

# 出力をnumpy配列に変換する
w, h = canvas.get_width_height()
image = np.frombuffer(canvas.tostring_rgb(), dtype='uint8').reshape((h, w, 3))

print(image.shape)  # (height, width, channels)
