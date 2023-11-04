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

with open("data.yaml", "r") as yaml_file:
    loaded_data = yaml.safe_load(yaml_file)

########################################

import yaml
with open("Best_trial.yaml", "w") as yaml_file:
    yaml.dump(Best_trial, yaml_file)
