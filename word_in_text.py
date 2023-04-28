###########################################

A=pd.DataFrame(columns=list(words_m),index=range(len(newsdata)))

for i in range(len(newsdata)):
    for j in range(len(words_m)):
        if list(words_m)[j] in wordsi[i]:
            A.iloc[i,j]=1
        else:
            A.iloc[i,j]=0

###########################################

A = pd.DataFrame(0, index=range(len(newsdata)), columns=words_m)

for i, text in enumerate(newsdata):
    for word in words_m:
        A.loc[i, word] = int(word in text)
        
###########################################
