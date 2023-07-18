#############################################

cell_colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (128, 0, 0),    # Maroon
    (0, 128, 0),    # Green (dark)
    (0, 0, 128),    # Navy
]

#############################################

#HEX CORDS
color_codes = [
    '#FF0000',  # Red
    '#FF4500',  # OrangeRed
    '#FF8C00',  # DarkOrange
    '#FFA500',  # Orange
    '#FFD700',  # Gold
    '#FFFF00',  # Yellow
    '#ADFF2F',  # GreenYellow
    '#7FFF00',  # Chartreuse
    '#00FF00',  # Lime
    '#00FA9A',  # MediumSpringGreen
    '#00FFFF',  # Cyan
    '#00BFFF',  # DeepSkyBlue
    '#0000FF',  # Blue
    '#8A2BE2'   # BlueViolet
]

hexc=color_codes[int(datai.iloc[j,5])%len(color_codes)]
c = tuple(int(hexc[i:i+2], 16) for i in (1, 3, 5))

#############################################
