
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


