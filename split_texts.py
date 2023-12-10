df = train
df['text1']=''
df['text2']=''
display(df)

for i in range(len(df)):
    texts=df.loc[i,'text'].replace('\n','')
    
    cts=texts.count('.')
    tex=texts.split('.')
    #print(cts)

    for t1 in tex[0:cts//2]:
        df.iloc[i,2]+=t1
    for t2 in tex[cts//2:-1]:
        df.iloc[i,3]+=t2

df1=df[['text1','target']]
df2=df[['text2','target']]
df1.columns=['text','target']
df2.columns=['text','target']
df3=pd.concat([df1,df2],axis=0)
display(df3)
train=df3

####################################


def split_text(df):
    df['text1']=''
    df['text2']=''
    for i in range(len(df)):
        texts=df.loc[i,'text'].replace('\n','')
        cts=texts.count('.')
        tex=texts.split('.')
        for t1 in tex[0:cts//2]:
            df.iloc[i,2]+=t1
        for t2 in tex[cts//2:-1]:
            df.iloc[i,3]+=t2
    df1=df[['text1','target']]
    df2=df[['text2','target']]
    df1.columns=['text','target']
    df3=pd.concat([df1,df2],axis=0)
    return df3




