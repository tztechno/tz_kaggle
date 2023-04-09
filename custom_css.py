
#https://raw.githubusercontent.com/JoseCaliz/dotfiles/main/css/vs_gruvbox.css

!wget http://bit.ly/3ZLyF82 -O CSS.css -q
    
from IPython.core.display import HTML
with open('./CSS.css', 'r') as file:
    custom_css = file.read()

HTML(custom_css)

