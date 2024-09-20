import random,json

test_list = ["success","failure"]

result = ""

for i in range(100):
    result += random.choice(test_list)+";"


with open("check.txt",'w') as f:
    f.write(result[:-1])

x = {
    "unit_test":"failed",
    "integration_test":"failed",
    "connection_test":"failed",
}

with open("tests/tests.json",'w') as file:
    json.dump(x,file,indent=1)
