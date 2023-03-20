from ipywidgets import interact, fixed

def square(x, y):
    return x ** 2 + y

interact(square, x=(0,10,1), y=fixed(5))



import ipywidgets as widgets
from ipywidgets.embed import embed_minimal_html
from IPython.display import display

slider = widgets.IntSlider(min=0, max=10, step=1, value=5)

# Display the widget in the notebook
display(slider)

# Generate an HTML file with the widget embedded
embed_minimal_html('slider.html', views=[slider])

