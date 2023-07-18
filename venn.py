from matplotlib_venn import venn2

# trainとtestでのnameの重複を確認する
f = 'name'
plt.figure(figsize=(3,3))
plt.title(f)
venn2(subsets=(set(df_train[f].unique()), set(df_test[f].unique())),
      set_labels=('Train', 'Test'))
plt.tight_layout()
