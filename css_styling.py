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
