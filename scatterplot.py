#############################################################################

import matplotlib.pyplot as plt
import seaborn as sns

for i in range(len(results)):
    ax=sns.scatterplot(data=data0[data0['i']==i], x="x", y="y", palette="Paired") 
    plt.title("Car Positions "+str(i).zfill(5))
    ax.set_xlim([0, 1200])
    ax.set_ylim([-700, 0])
    plt.savefig('./sample3/fig_'+str(i).zfill(5)+'.png')
    
#############################################################################

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig=make_subplots(specs=[[{"secondary_y":False}]])
fig.add_trace(go.Scatter(x=data1['date'][682:],y=data1['positives mean'][682:],name='positives mean'),secondary_y=False,)
fig.update_layout(autosize=False,width=700,height=500,title_text="Examined Positives (rolling 7-day) in Tokyo")
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Cases",secondary_y=False)
fig.show()

#############################################################################
