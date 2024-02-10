from PIL import Image
width, height = 100,100
background_color = (0,0,0)
image = Image.new("RGB", (width,height), background_color)
text='abc'
image.save(f"{text}.png")
