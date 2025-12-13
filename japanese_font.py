
!wget https://moji.or.jp/wp-content/ipafont/IPAexfont/ipaexg00401.zip
!unzip ipaexg00401.zip

from matplotlib import font_manager, rcParams

font_path = "ipaexg00401/ipaexg.ttf"
font_manager.fontManager.addfont(font_path)
rcParams["font.family"] = "IPAexGothic"
rcParams["axes.unicode_minus"] = False

---------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib import font_manager, rcParams

def set_japanese_font():
    candidates = [
        "IPAexGothic",
        "IPAGothic",
        "Noto Sans CJK JP",
        "Noto Serif CJK JP",
        "TakaoGothic",
        "Yu Gothic",
        "Hiragino Sans",
        "MS Gothic",
        "Meiryo"
    ]

    for font in font_manager.findSystemFonts():
        font_prop = font_manager.FontProperties(fname=font)
        name = font_prop.get_name()
        if name in candidates:
            rcParams["font.family"] = name
            rcParams["axes.unicode_minus"] = False
            print(f"✔ Japanese font set: {name}")
            return

    raise RuntimeError("日本語フォントが見つかりません")

set_japanese_font()
