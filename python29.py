import json
data = '''
{ "name" : "chuck",
"phone" : { 
"type" : "intl", 
"number" : "+1 786 293 9289"}, 
 "email" : { 
    "hide" : "yes" }        
      }'''

info = json.loads(data)
print('Name: ',info["name"])
print('Hide:', info["email"]["hide"])