##############################

n=len(data_df3)
N=list(range(n))
random.seed(100)
M=random.sample(N,3000)
data_df4=data_df3.iloc[M].reset_index(drop=True)

##############################
