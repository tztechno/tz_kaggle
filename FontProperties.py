import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

bengali_font_path = '/path/to/bengali/font.ttf' 
bengali_font = FontProperties(fname=bengali_font_path)

plt.plot([1, 2, 3], [4, 5, 6])
title_text = "আমার শিরোনাম"
plt.title(title_text, fontproperties=bengali_font)
plt.show()

