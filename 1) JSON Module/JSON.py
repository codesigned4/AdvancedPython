import json
import os 
print(os.getcwd())
#Dict to JSON
personDict={"name":"ali","languages":["python","C#"]}
result=json.dumps(personDict,indent=4,sort_keys=True)

#JSON to Dict
personJSON='{"name":"ali","languages":["python","C#"]}'
result=json.loads(personJSON)

#from JSON file to Dict
with open("person.json","r") as f:
    result=json.load(f)
print(result)

#from Python file (as Dict) to JSON
with open("newfile.json","w") as f:
    json.dump(personDict,f,indent=4)

