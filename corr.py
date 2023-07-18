# ヒートマップで相関係数を調べます
df_train.corr().style.background_gradient(cmap = "bwr", vmin = -1, vmax = 1, axis = None)
