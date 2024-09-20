# check if the success rate is > 50%
import json

result = "failed"
f = open("check.txt","r").read()

l = f.split(";")

success_rate = l.count("success")

assert success_rate > 50 , f"failed unit test success rate is {success_rate/100}"


with open("tests/tests.json",'r') as file:
    data = json.load(file)

data["unit_test"] = "passed"

with open("tests/tests.json",'w') as file:
    json.dump(data,file,indent=1)

print(f"well done success rate is {success_rate/100}")