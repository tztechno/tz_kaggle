import math
from sklearn.linear_model import LinearRegression
mod = LinearRegression()
def modscore(x,y):
    R2=mod.score(x,y)
    return R2

df_x=pd.DataFrame(testY)
df_y=pd.DataFrame(preds2)
mod_lin = mod.fit(df_x, df_y)
y_lin_fit = mod_lin.predict(df_x)
r2_lin = mod.score(df_x, df_y)

fig,ax = plt.subplots(figsize=(6,6))
ax.set_title('Prediction Result of Yield',fontsize=20)
ax.set_ylabel('predicted',fontsize=12)
ax.set_xlabel('actual',fontsize=12)
ax.scatter(testY,preds2,alpha=0.4)

plt.text(10,7,'$ R^{2} $=' + str(round(r2_lin, 4)))
plt.plot(df_x, y_lin_fit, color='black', linewidth=0.5)
plt.show()
