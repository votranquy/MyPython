
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit =iter(mystr)
for x in range(len(mystr)):
    print(next(myit))

mytuple = ("apple","banana","cherry")
for x in mytuple:
    print(x)