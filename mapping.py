################

mapping_dict = movies.set_index("Movie_ID")["Name"].to_dict()

################

Name=data['Species'].unique().tolist()
N=list(range(len(Name)))
normal_mapping=dict(zip(Name,N)) 
reverse_mapping=dict(zip(N,Name))       
data['Species']=data['Species'].map(normal_mapping)

################


