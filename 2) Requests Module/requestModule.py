import requests
import json

result=requests.get("https://jsonplaceholder.typicode.com/todos")
#prints <Response [200]> 
result=result.text
#prints the source code of whatever type it is generated
result=json.loads(result)
#we turn into dict type so it prints source code as dictionary type
print(result["userId"])