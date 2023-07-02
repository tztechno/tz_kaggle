#######################################################################
###go.Scatter

import plotly.graph_objects as go

fig = go.Figure()
for col in cols:
    fig.add_trace(go.Scatter(x=data4.index, y=data4[col], mode='markers+lines', name=col))
fig.update_layout(
    xaxis=dict(title='Day', tickangle=90),
    yaxis=dict(title='Rating'),
    title='Rating Change'
)
fig.show()

#######################################################################
###plt.subplots

fig, ax = plt.subplots(figsize=(12, 10))
for col in cols:
    ax.plot(data4.index, data4[col], marker='o', label=col)
ax.set_xlabel('Day')
ax.set_ylabel('Rating')
ax.set_title('Rating Change')
ax.set_xticks(data4.index)
ax.set_xticklabels(data4.index, rotation=90)
ax.legend()
plt.show()

#######################################################################
###plt.plot

plt.figure(figsize=(12,10))
for col in cols:
    plt.plot(data4.index,data4[col],marker='o',label=col) 
plt.xlabel('Day')
plt.ylabel('Rating')
plt.title('Rating Change')
plt.xticks(rotation=90)
plt.xticks(data4.index)
plt.legend() 
plt.show()

#######################################################################
