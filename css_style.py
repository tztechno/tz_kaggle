################################

https://github.com/JoseCaliz/dotfiles/tree/main/css

https://github.com/JoseCaliz/dotfiles/blob/main/css/gruvbox.css
https://github.com/JoseCaliz/dotfiles/blob/main/css/gruvbox_complete.css
https://github.com/JoseCaliz/dotfiles/blob/main/css/monokai.css
https://github.com/JoseCaliz/dotfiles/blob/main/css/vs_gruvbox.css

!wget https://raw.githubusercontent.com/JoseCaliz/dotfiles/main/css/gruvbox.css -O CSS.css -q
!wget https://raw.githubusercontent.com/JoseCaliz/dotfiles/main/css/gruvbox_complete.css -O CSS.css -q
!wget https://raw.githubusercontent.com/JoseCaliz/dotfiles/main/css/monokai.css -O CSS.css -q
!wget https://raw.githubusercontent.com/JoseCaliz/dotfiles/main/css/vs_monokai.css -O CSS.css -q

!wget http://bit.ly/3ZLyF82 -O CSS.css -q
    
################################

!wget https://raw.githubusercontent.com/JoseCaliz/dotfiles/main/css/vs_monokai.css -O CSS.css -q
    
from IPython.core.display import HTML
with open('./gruvbox.css', 'r') as file:
    custom_css = file.read()

HTML(custom_css)

################################

!wget http://bit.ly/3ZLyF82 -O CSS.css -q
    
from IPython.core.display import HTML
with open('./CSS.css', 'r') as file:
    custom_css = file.read()

HTML(custom_css)

################################

