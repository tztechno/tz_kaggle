#########################

usei = data_df2[data_df2.iloc[:,3].isin(signs)].index
data_df3 = data_df2.loc[usei]

#########################

usei=[]
for i in range(len(data_df2)):
    if data_df2.iloc[i,3] in signs:
        usei+=[i]
data_df3=data_df2.iloc[usei]

#########################
