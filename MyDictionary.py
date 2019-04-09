
# #Python dictionaries
# thisdict = {
#     "brand":"Ford",
#     "model":"Mustag",
#     "year":1976
# }
# print(thisdict) #{'brand': 'Ford', 'model': 'Mustag', 'year': 1976}


# #acces the item
# x=thisdict["model"]
# print(x)

# x=thisdict.get("model")
# print(x)

# #change the value
# thisdict["year"]=2019
# print(thisdict)

# #loop to get the attribute AND value
# for x in thisdict:
#     print(x) #brand model year

# for x in thisdict:
#     print(thisdict[x]) # Ford Mustag 2019

# for x in thisdict.values():
#     print(x)          # Ford Mustag 2019
    
              
# for x,y in thisdict.items():
#     print(x,y)  #('brand', 'Ford')('model', 'Mustag')('year', 2019)

# #check if key exists
# if "model" in thisdict:
#     print("yes, 'model' is one keys of thislist")


# ##len() 
# thisdict = {
#     "brand":"Ford",
#     "model":"Mustag",
#     "year":1976
# }  
# print(len(thisdict)) #3


# #Add to dic
# thisdict['color'] ="red"
# print(thisdict) #Random order
# thisdict['price'] ="32000$"
# print(thisdict) #Random order


# #Remove dic
# thisdict.pop("brand")
# print(thisdict)

# #Remove =>#BUTthe first items => item[0]
# print(thisdict)
# thisdict.popitem()
# print(thisdict)


# #= Remove (Del keyword) 
# del thisdict["model"]
# print(thisdict)


# # #Del can not use if the dic have only one element
# # #ERROR when using: del thisdict


# #Empty the dic
# thisdict.clear()
# print(thisdict) #{}


# #Copy a dict
# thisdict = {
#   'dad':'John',
#   'mom':'Lie',
#   'son':'Tom'
# }
# mydict = thisdict.copy()
# print(mydict)

# thisdict = {
#   'dad':'John',
#   'mom':'Lie',
#   'son':'Tom'
# }
# mydict = dict(thisdict)
# print(mydict)



# #Constructor dic
# thisdict = dict(brand="Ford",model="Mustag",color="RED")
# print(thisdict)

# #fromkey()

# position = ('dad', 'mom', 'son')
# name = 0#('John', 'lee', 'Tom')
# thisdict = dict.fromkeys(position,name))
# print(thisdict)

#get()

thisdict = {
  'dad':'John',
  'mom':'Lie',
  'son':'Tom'
}
print(thisdict.get('dad'))