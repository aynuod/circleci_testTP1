import json

f = open("tests/tests.json","r").read()

json_data = json.loads(f)

t1 = json_data["unit_test"]
t2 = json_data["integration_test"]
t3 = json_data["connection_test"]

if all(test == "passed" for test in [t1,t2,t3]):
    print(f"all test are passed !")
else:
    s = ""
    for i in json_data.keys():
        s += f"{i} {json_data[i]} , "
    print(s)