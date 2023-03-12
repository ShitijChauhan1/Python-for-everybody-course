import json
input= '''[
{"id" : "001",
 "x" : "2",
 "name" : "chuck"
  },
{"id" : "009",
 "x" : "7",
 "name" : "brent"
  }
]'''

data = json.loads(input)
print("user count: " , len(data))
for user in data:
    print("Name: ", user["name"])
    print("Id: ", user["id"])
    print("Attribute", user["x"])