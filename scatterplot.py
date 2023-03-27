
import matplotlib.pyplot as plt
import seaborn as sns

for i in range(len(results)):
    ax=sns.scatterplot(data=data0[data0['i']==i], x="x", y="y", palette="Paired") 
    plt.title("Car Positions "+str(i).zfill(5))
    ax.set_xlim([0, 1200])
    ax.set_ylim([-700, 0])
    plt.savefig('./sample3/fig_'+str(i).zfill(5)+'.png')
    
    
