import yaml

plate_yaml = dict(
    train ='train',
    val ='valid',
    test='test',
    nc =26,
    names = NameList
)

with open('plate.yaml', 'w') as outfile:
    yaml.dump(plate_yaml, outfile, default_flow_style=True)
    
%cat plate.yaml
