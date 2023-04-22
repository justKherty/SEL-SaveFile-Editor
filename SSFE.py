import subprocess
import json

subprocess.run(["python", "SSFE_JSON_Convert.py"])

with open("output.json", "r") as f:
    data = json.load(f)

subprocess.run(["python", "SSFE_main.py"])

with open("output.json", "w") as f:
    json.dump(data, f)
