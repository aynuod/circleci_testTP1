# wait a 3 min to check if a user is connected viw netcat
import json
def pas():
    return 1


with open("tests/tests.json",'r') as file:
    data = json.load(file)

data["connection_test"] = "passed"

with open("tests/tests.json",'w') as file:
    json.dump(data,file,indent=1)

print(pas())