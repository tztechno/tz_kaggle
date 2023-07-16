################################

!wget https://raw.githubusercontent.com/JoseCaliz/dotfiles/main/css/gruvbox.css 2>/dev/null 1>&2
!pip install feature_engine 2>/dev/null 1>&2
    
from IPython.core.display import HTML
with open('./gruvbox.css', 'r') as file:
    custom_css = file.read()

HTML(custom_css)

################################

# CSS style setting
!wget http://bit.ly/3ZLyF82 -O CSS.css -q
    
from IPython.core.display import HTML
with open('./CSS.css', 'r') as file:
    custom_css = file.read()

HTML(custom_css)

################################
