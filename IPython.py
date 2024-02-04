####################################################

htmls=[]
for item in paths2:
    htmls+=["<iframe width='600' height='400' src='" +item+ "' frameborder='0'></iframe>"]

IPython.display.HTML(htmls[5])

####################################################


IPython.display.IFrame(paths0[i],800,400)


####################################################
