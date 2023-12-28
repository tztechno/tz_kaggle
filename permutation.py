
p = Permutation([0, 2, 3, 1])
rp=p**-1
#Permutation(1, 2, 3)

# normal mapping
normal_map={i: p(i) for i in range(p.size)}
#{0: 0, 1: 2, 2: 3, 3: 1}
#reverse mapping
reverse_map={p(i): i for i in range(p.size)}
#{0: 0, 1: 3, 2: 1, 3: 2}

N0=[0,1,2,3]
N1=[normal_map[i] for i in N0]
N2=[reverse_map[i] for i in N1]
print(N0,N1,N2)
#[0, 1, 2, 3] [0, 2, 3, 1] [0, 1, 2, 3]

p([0,1,2,3])
#[0, 2, 3, 1]
rp([0, 2, 3, 1])
#[0, 1, 2, 3]

p(['A', 'B', 'C', 'D'])
#['A', 'C', 'D', 'B']
rp(['A', 'C', 'D', 'B'])
#['A', 'B', 'C', 'D']



########################################

# approach1 for name2perm_map
info=pd.read_csv('/kaggle/input/santa-2023/puzzle_info.csv')
display(info)

names=[]
perms=[]
dic=ast.literal_eval(info.iloc[0,1])
df=pd.DataFrame(dic)
n=len(df)
N=list(range(n))
cols=df.columns.tolist()

for col in cols:
    p=Permutation(df.loc[:,col].tolist())
    rp=p**-1
    df['-'+col]=rp(N)
    perms+=[p,rp]
    names+=[col,'-'+col]

print(names)
print(perms)

name2perm_map=dict(zip(names,perms)) 
print(name2perm_map)


########################################

# approach2 for name2perm_map
df=pd.read_csv('/kaggle/input/santa-2023-create-permutation-and-mapping/cube_222.csv')
display(df)
names=df['move'].tolist()

perms=[]
for i in range(len(df)):
    p=Permutation(ast.literal_eval(df.loc[i,'list']))
    perms+=[p]
    
name2perm_map=dict(zip(names,perms)) 
print(name2perm_map)



########################################


