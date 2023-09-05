################

mapping_dict = movies.set_index("Movie_ID")["Name"].to_dict()

################

idx2eco = data0['economy'].to_dict()
print(idx2eco)
eco2idx = {v: k for k, v in idx2eco.items()}
print(eco2idx)

################

Name=data['Species'].unique().tolist()
N=list(range(len(Name)))
normal_mapping=dict(zip(Name,N)) 
reverse_mapping=dict(zip(N,Name))       
data['Species']=data['Species'].map(normal_mapping)

################

class_names = ['paper', 'rock', 'scissors']
N = list(range(len(class_names)))
normal_mapping = dict(zip(class_names, N)) 
reverse_mapping = dict(zip(N, class_names))    

################

