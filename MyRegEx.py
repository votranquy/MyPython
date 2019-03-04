import re
txt = "The rain in Spain"
x = re.search("^The.*Spain",txt)
if(x):
    print("YES")
else:
    print("NO")

print("++++++++++++")
str = "The rain in Spain"
x = re.findall("\AThe",str)
print(x)
if(x):
    print("Yes")
else:
    print("NO")

print("++++++++++++")
str = "The rain in Spain"
x = re.findall("ai",str)
print(x)

print("++++++++++++")
str = "The rain in Spain"
x = re.search("\s",str)
print("The first white-space character is located at position: ", x.start())

print("++++++++++++")
str = "The rain in Spain"
x = re.split("\s",str)
print(x)
print("++++++++++++")
str = "The rain in Spain"
x =re.split("\s",str,1)
print(x)

print("++++++++++++")
str = "The rain in Spain"
x = re.sub("\s","9",str)
print(x)

print("++++++++++++")
str = "The rain in Spain"
x =re.sub("\s","9",str,2)
print(x)

print("++++++++++++")
str="The rain in Spain"
x= re.search("ai",str)
print(x)

print("++++++++++++")
str = "The rain in Spain"
x = re.search(r"\bS\w+",str)
print(x.span())
print("++++++++++++")
str = "The rain in Spain"
x = re.search(r"\bS\w+",str)
print(x.string)

print("++++++++++++")
str= "The rain in Spain"
x = re.search(r"\b\S\w+",str)
print(x.group())
