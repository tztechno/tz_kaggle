train = data1[data1['x_e_out [-]'].notna()]
test = data1[data1['x_e_out [-]'].isna()]

###############################################

df_numeric.info()
df_numeric.isnull().sum()
df_numeric.dropna(inplace=True)


###############################################




