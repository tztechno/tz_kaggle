
##############################

plt.figure(figsize=(5,5)) 
plt.title('Purchased vs Age',fontsize=16)
plt.xlabel('Purchased',fontsize=12)
plt.ylabel('Age',fontsize=12)
plt.scatter( df['Purchased'],df['Age'],alpha=0.1) 
plt.show()


##############################

fig,ax = plt.subplots(figsize=(5,5))
ax.set_title(target[0],fontsize=16)
ax.set_ylabel('Test_pred',fontsize=12)
ax.set_xlabel('Test_true',fontsize=12)
ax.scatter(y_true,y_pred,alpha=0.2)
plt.show()

##############################
