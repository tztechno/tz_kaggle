def RevSort(S):
    S2=[]
    for i,j in zip(S,col):
        S2+=[(i,j)]
    S2.sort(reverse=True)
    S3=''
    for si in S2:
        S3+=si[1]
    return S3 

S=[3,6,2,9]
col=['A','B','C','D']
RevSort(S)
