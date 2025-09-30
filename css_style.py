################################

<div style="border:2px solid red; padding:10px; border-radius:5px; font-weight:bold;">

  This whole text becomes bold automatically.
  You don’t need ** to wrap each part.
    
</div>

################################

<div style="border: 2px solid red; padding:10px; border-radius:5px;">
  
This cell content has a **red border** but transparent background.  

</div>

################################

<div style="background-color: lightyellow; padding: 10px;">

<div style="background-color: lightyellow; font-size: 18px; padding: 10px;">

################################

from IPython.display import display, HTML

display(HTML('''
<style>
div.text_cell_render {
    background-color: lightyellow;
    padding: 20px;
}
</style>
'''))


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
!wget https://raw.githubusercontent.com/JoseCaliz/dotfiles/main/css/vs_gruvbox.css -O CSS.css -q  

################################

!wget https://raw.githubusercontent.com/JoseCaliz/dotfiles/main/css/vs_gruvbox.css -O CSS.css -q  
!wget http://bit.ly/3ZLyF82 -O CSS.css -q
 
################################

!wget http://bit.ly/3ZLyF82 -O CSS.css -q

from IPython.core.display import HTML
with open('./CSS.css', 'r') as file:
    custom_css = file.read()
HTML(custom_css)

################################

