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
colors=[]
for c in color_codes:
    colors += [tuple((int(c[1:3],16),int(c[3:5],16),int(c[5:7],16)))] 
print(colors)
#[(255, 0, 0), (255, 69, 0), (255, 140, 0), (255, 165, 0), (255, 215, 0), 
#(255, 255, 0), (173, 255, 47), (127, 255, 0), (0, 255, 0), (0, 250, 154), 
#(0, 255, 255), (0, 191, 255), (0, 0, 255), (138, 43, 226)]

#############################################
#color bar, color circle

lower_color = np.array(min_nc[0])  # lower RGB value
upper_color = np.array(max_nc[0])  # upper RGB value

# RGB variation
color_variations = np.linspace(lower_color, upper_color,72)

fig, ax = plt.subplots(figsize=(10,5))
ax.imshow([color_variations.astype(int)])
ax.axis('off')
plt.show()

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
ax.pie([1] * len(color_variations), colors=color_variations/255, startangle=90, counterclock=False)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.axis('off')
plt.show()

#############################################
