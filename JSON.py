#Convert from JSON to Python

import json

#Some JSON
val = '{"name":"Rakib", "age":24, "City":"Dhaka", "Uni":"ISTT"}'

#parse val

new_val= json.loads(val)

#The result is a python dictionary
print(new_val)
print(new_val["name"])
print(new_val["age"])



#Convert from Python to JSON
Capital={
	"Ban": "Dhaka",
	"USA": "Wasington DC",
	"Canada": "Toranto",
	"Germany":"Berlin",
	"independent":1971,
	"Muslim": True

}
print(Capital.values())
print(Capital.keys())

#Convert into JSON
conv=json.dumps(Capital, indent=4)

#the result is a JSON string
print("The JSON file is :"+conv)