///////////////////////////////////////////

N,C,D,H,W = 60,3,10,100,100
paths=[]
for i in range(600):
    r=i//10
    c=i%10
    datai = torch.randint(low=0, high=256, size=(3,100,100), dtype=torch.uint8)
    path='./data/'+str(r).zfill(3)+'_'+str(c).zfill(3)+'.pt'
    paths+=[path]
    torch.save(datai,path)
label = [0,1,2]
label = np.random.randint(0,3,size=(60,))
labels = pd.DataFrame(columns=['id','label'])
labels['id']=list(range(60))
labels['label']=label
labels.to_csv('labels.csv',index=False)

///////////////////////////////////////////

!mkdir train
!mkdir test
labels = ['a','b','c']
for L in labels:
    !mkdir train/{L}
    !mkdir test/{L}
    
dirs=['train','test']
N,C,H,W = 400,3,100,100

paths=[]
for i in range(400):
    k=i//300
    p=i%3
    datai = torch.randint(low=0, high=256, size=(3,100,100), dtype=torch.uint8)
    path=f'./{dirs[k]}/{labels[p]}/'+str(i).zfill(3)+'.pt'
    paths+=[path]
    torch.save(datai,path)

///////////////////////////////////////////
