import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig=make_subplots(specs=[[{"secondary_y":False}]])
fig.add_trace(go.Scatter(x=data1['date'],y=data1['positives mean'],name='positives mean'),secondary_y=False,)
fig.add_trace(go.Scatter(x=data1['date'],y=data1['positives max'],name='positives max'),secondary_y=False,)
fig.add_trace(go.Scatter(x=data1['date'],y=data1['positives min'],name='positives min'),secondary_y=False,)

fig.update_layout(autosize=False,width=700,height=500,title_text="Examined Positives (rolling 7-day) in Tokyo")
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Cases",secondary_y=False)
fig.show()
