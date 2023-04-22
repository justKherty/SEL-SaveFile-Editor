#NON FUNCTIONAL!!!

import json

input_file_name = "INPUT.json"
output_file_name = "OUTPUT.json"

#key_to_compare = "Cou041"

# Read in the input file
with open(input_file_name, "r") as f:
    input_data = json.load(f)

try:
    with open(output_file_name, "r") as f:
        output_data = json.load(f)
except FileNotFoundError:
    output_data = {}

if key_to_compare in input_data and key_to_compare in output_data:
    if input_data[key_to_compare]["is_viewed"] == 0 and output_data[key_to_compare]["is_viewed"] == 1:
        input_data[key_to_compare]["is_viewed"] = 1
elif key_to_compare in input_data:
    output_data[key_to_compare] = {"is_viewed": 0}

with open(input_file_name, "w") as f:
    json.dump(input_data, f, indent=4)
with open(output_file_name, "w") as f:
    json.dump(output_data, f, indent=4)
