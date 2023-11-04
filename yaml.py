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


########################################

import yaml

data = {"key1": "value1", "key2": "value2"}

with open("data.yaml", "w") as yaml_file:
    yaml.dump(data, yaml_file)
