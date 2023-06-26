
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def fig_show(i):    
    fig=make_subplots(specs=[[{"secondary_y":False}]])
    namesi=NAMES[i]
    for name in namesi:
        datai=data2[data2['name']==name]
        fig.add_trace(go.Scatter(x=datai['date'],y=datai['pts'],name=name[0:14]),secondary_y=False,)
    fig.update_layout(autosize=False,width=700,height=500,title_text='Ranking '+str(i+1))
    fig.update_xaxes(title_text='date')
    fig.update_yaxes(title_text="pts",secondary_y=False)
    fig.show(renderer='iframe')
  
