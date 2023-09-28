def rgb_to_hex(rgb):
    # RGB成分を16進数に変換して連結し、#を付ける
    return "#{:02X}{:02X}{:02X}".format(rgb[0], rgb[1], rgb[2])

# RGBコードを指定
rgb_color = (255, 0, 0)  # 例: 赤色

# RGBからHEXに変換
hex_color = rgb_to_hex(rgb_color)

# 結果を表示
print("RGB:", rgb_color)
print("HEX:", hex_color)
