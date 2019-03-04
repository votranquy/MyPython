import json
#CONVERT FROM JSON TO PYTHON
    #Some JSON:
x = '{"name":"John","age":30,"city":"New York"}'
    #parse x:
print(x)    
   
y = json.loads(x)
    #the result is a Python dictionary:
print(y["age"])
print("+++++++++++++++++++")
#CONVERT FROM PYTHON TO JSON
x = {
    "name":"Le",
    "age":30,
    "city":"HCM city"
}
print(x["age"])
y = json.dumps(x)

print(y)
    #some type of convert Python to JSON
print("+++++++++++++++++++")
print(json.dumps({"name":"John","age":40}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("apple","banana")))
print(json.dumps(45))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
    #some examples
print("+++++++++++++++++++")
x = {
    "name":"John",
    "age":40,
    "married":True,
    "children":("Ann","Bob"),
    "pet": None,
    "cars": [
        {"model":"BMW 2013","mpg":27.5},
        {"model":"Ford Edge","mpg":28.1}
    ]
}

print(json.dumps(x))
print(json.dumps(x,indent=4))
print(json.dumps(x,indent=4,separators=(". "," = ")))
print(json.dumps(x,indent=4,sort_keys=True))