import json

with open('INPUT.txt', 'r') as f:
    variables = f.read()

variables = variables.replace(' ', '').replace('\n', '')

variables_list = variables.split(',')

variables_dict = {}

for variable in variables_list:
    key, value = variable.split(':')
    key = key.replace('"', '')
    value = value.replace('"', '')
    value = int(value)
    variables_dict[key] = {"is_viewed": value}

json_str = json.dumps(variables_dict)
print(json_str)
