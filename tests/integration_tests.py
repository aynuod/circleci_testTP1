# check the connection to db (example MongoDB)

import pymongo , json
from pymongo import MongoClient

result = "failed"

mongo_uri = "mongodb+srv://imadxt:imad2002@imadxtserver.rplm1sg.mongodb.net/?retryWrites=true&w=majority&appName=imadxtServer"

client = MongoClient(mongo_uri)

db = client['circleciDB'] 

collection = db['circleci'] 


res = collection.find_one({"user":"root"})


assert res != None, "no root user in your database"

with open("tests/tests.json",'r') as file:
    data = json.load(file)

data["integration_test"] = "passed"

with open("tests/tests.json",'w') as file:
    json.dump(data,file,indent=1)

print("root exist, integration test passed successfuly")
