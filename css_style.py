################################

https://github.com/JoseCaliz/dotfiles/tree/main/css

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

### CSS for notebook styling ###
from IPython.core.display import HTML

HTML('''
<style>
    :root {
        --box_color: #FEFCF3;
    }
    body[data-jp-theme-light="true"] .jp-Notebook .CodeMirror.cm-s-jupyter{
        background-color: var(--box_color) !important;
    }
    div.input_area{
        background-color: var(--box_color) !important;
    }
</style>
''')

################################
