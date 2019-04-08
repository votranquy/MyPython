# print("Hello world")
# #Use a Tad to mark a block of code
# if 5 > 2:
#     print("Of course, 5>2")
# #creating a Variable
# x = 5
# y = "John"
# print(x)
# print(y)
# #change type. It's easy
# x = 4
# x = "Sally"
# print(x)
# #Variable
# #1. Start with _ (underscore) or letter NOT number
# #2. Only contain alpha-numeric character and underscore (A-z, 0-9, _)
# #3. Case-sensitive (age and Age are different)
# x = "awesome"
# print("Python is " + x)

# x = "Python is "
# y = "awesome"
# z = x +y
# print(z)

# x = 5
# y = 10
# print(x + y)

# #Can not use "+" to combine variables being deferent type
# # x = 5
# # y = "John"
# # print(x + y)
# # Error

# #PYTHON NUMBER
# # have int, float, complex
# x = 1 #int
# y = 2.8 #float
# z = 1j+5 #complex
# print(x)
# print(type(x))
# print(y)
# print(type(y))
# print(z)
# print(type(z))

# #INT
# x = 2
# y = 234834530
# z = -1939939
# print(type(x))
# print(type(y))
# print(type(z))
# #FLOAT
# x = 1.1
# y = 1.0
# z = -19.39939
# print(type(x))
# print(type(y))
# print(type(z))
# x =35e4
# y= 12E5
# z = -34E2
# print(type(x))
# print(type(y))
# print(type(z))
# #COMPLEX
# x = 3+5j
# y = 5j
# z = -34j
# print(type(x))
# print(type(y))
# print(type(z))

# x = int(1)
# y = int(-1.9)
# z = int("3")
# print(x)
# print(y)
# print(z)

# x = float(1)
# y = float(2.5)
# z = float("4")
# w = float("5.7")

# x = str("s1")
# y = str(3)
# z = str(3.7)

# a = "Heello"
# print(a[0]) #Begin from 0
# print(a[0:2]) #Get from 0 to 1 (2-1)

# a="    Hello   you   "
# print(a)
# print(a.strip()) #No have space at begining and ending
# a = "Hello World"
# print(len(a))
# a = "Hello World"
# print(a.upper())
# a = "Hellow WOrld"
# print(a.replace("H","J"))
# a = "hello, world"
# print(a.split(","))


#Command-line String Input
# x = 1
# print("Enter your name:")
# x = input()
# print("Hello, " + x)

# x= 2
# y= 3
# print(x**y) #2^3 = 8
# x=5
# print(x)
# x+=5
# print(x) #10
# x-=5
# print(x) #5
# x*=5
# print(x) #25
# x/=5
# print(x) #5
# x%=3
# print(x) #5%3 chia lay du: 2
# x=7
# x//=2 #Chia lay ket qua va lam tron thap #
# print(x) #3
# x=3
# x**=2 #3^2 =9
# print(x) #9
# x&=3  #9&3 =1
# print(x)#1
# x|=4 
# print(x) #1|4 = 5
# x^=3
# print(x) #5 ^ 3 = 6
# x>>=1
# print(x) #3
# x<<=2
# print(x) #12



# x = 5
# print(x > 3 and x < 10) #True
# print(x > 3 or x < 10) #True
# print(not(x > 3 or x < 10)) #False




# x = ["apple", "banana"]
# print("pineapple" not in x) #True
# x = ["apple", "banana"]
# print("banana" in x) #True



# x= 5
# print(x>3 or x<4)
# x=5
# print(not(x>3 and x<10))



# #LIST
# thislist = ["apple","banana","Cherry"] #['apple', 'banana', 'Cherry']
# print(thislist)
# print(thislist[1])
# thislist[1]="orange" #Change the second item
# print(thislist)
# for x in thislist:
#     print(x)

# thislist = ["apple","banana","cherry"]
# if "apple" in thislist:
#     print("Yes, apple is in this list")
# if "mango" not in thislist:
#     print("Mango is not in thislist")

# thislist = ["apple","banana","cherry"]
# print("Do dai cua thislist la:") 
# print(len(thislist))    

# thislist = ["apple","banana","cherry"]
# thislist.append('orange')
# print(thislist)   

# thislist = ["apple","banana","cherry"]
# thislist.insert(1,"orange")
# print(thislist)  

# thislist = ["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)  

# thislist = ["apple","banana","cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple","banana","cherry"]
# del thislist[0]
# del thislist[0]
# print(thislist)

# thislist = ["apple","banana","cherry"]
# del thislist

# # thislist = ["apple","banana","cherry"]
# # thislist.clear()
# # thislist.append("SamSung")
# # print(thislist)

# thislist =list(("apple","banana","cherry"))
# print(thislist) 


# thistuple = ("Car", "House", "Love")
# print(thistuple)

# thistuple = ("Car", "House", "Love")
# print(thistuple[1])

# # thistuple = ("Car", "House", "Love")
# # thistuple[1] = "Land"
# # print(thistuple)
# # thistuple = ("apple", "banana", "cherry")
# # thistuple[1] = "blackcurrant"
# # # The values will remain the same:
# # print(thistuple)
# thistuple = ("Car", "House", "Love")
# for x in thistuple:
#     print(x)

# thisproperty = ("Car","Hourse","Love")
# for x in thisproperty:
#     print(x)

# thisproperty = ("Car","Hourse","Love")
# # thisproperty[1] = "Money"
# print(thisproperty)

# thistuple=("apple","Samsung","nokia")
# if "apple" in thistuple:
#     print("Yes, 'apple' is in this list")

# thistuple = ('apple','samsung','nokia')
# print(len(thistuple))
# #Can not add items to tuple
# #Can not remove items in a tuple
# # Use del to delete all tuple

# thistuple = tuple(("apple", "samsung","nokia"))
# print(thistuple)
# print(thistuple.count("apple"))
# print(thistuple.index("nokia"))

# thisset={"apple","banana","cherry"}
# for x in thisset:
#     print(x)

# thisset = {'apple','banana', 'cherry'}
# print("banana" in thisset)

# #Can not change the ites in set
# #But Can add new items

# thisset = {'apple',"banana",'cherry'}
# thisset.add("orange")
# print(thisset)

# thisset ={'apple','banana','cherry'}
# thisset.update(['startfruit','dragonfruit','orange'])
# print(thisset)

# thisset = {'apple','mango'}
# print(len(thisset))

# thisset = {'apple','mango'}
# thisset.remove('mango')
# print(thisset)
# thisset.discard("apple")
# print(thisset)

# thisset = {'apple','banana','cherry'}
# x = thisset.pop()
# print(x)
# print(thisset)

# thisset = {'apple','banana','cherry'}
# x = thisset.pop()
# print(x)
# print(thisset)

# thisset ={'apple',"mango"}
# thisset.clear()
# print(thisset)

# # thisset = {"apple","mango"}
# # del thisset
# # print(thisset)

# thisset = set(("apple","banana","cherry"))
# print(thisset)
# #https://www.w3schools.com/python/python_sets.asp


# #Python dictionaries
# thisdict ={
#     "brand":"Ford",
#     "model":"Mustag",
#     "year":1976
# }
# print(thisdict)
# x=thisdict["model"]
# print(x)
# x=thisdict.get("model")
# print(x)
# thisdict["year"]=2019
# print(thisdict)
# for x in thisdict:
#     print(x)
# for x in thisdict:
#     print(thisdict[x])
# for x in thisdict.values():
#     print(x)
# for x,y in thisdict.items():
#     print(x,y)
# for x,y in thisdict.items():
#     print(x,y)
# if "model" in thisdict:
#     print("yes, 'model' is one keys of thislist")
# print(len(thislist))
# #Add to dic
# thisdict['color'] ="red"
# print(thisdict)
# #Remove dic
# thisdict.pop("color")
# print(thisdict)
# #Remove the last
# thisdict.popitem()
# print(thisdict)
# #Del keyword
# del thisdict["brand"]
# print(thisdict)
# #Del can not use if the dic have only one element

# #Empty the dic
# thisdict.clear()
# print(thisdict)
# #Constructor dic
# thisdict = dict(brand="Ford",model="Mustag")
# print(thisdict)



# #PYthon If Else
# a=33
# b=200
# if b>a :
#     print("b is great than a")

# # Elif  
# a=33
# b=33
# if b>a:
#     print("b is great than a")
# elif a==b:
#     print("a and b are equal")
# #Else (the final catch) not have the condition
# a =200
# b =33
# if b>a:
#     print("b > a")
# elif a==b:
#     print("a =b")
# else:
#     print("a > b")
# #One line
# if a>b: print("a is greater than b")

# #If Else short hand
# # a =200
# # b=300
# # print("a") if a > b else print("b")

# a=330
# b=330
# print("A") if a>b else print("=") if a==b else print("B")

# a=200
# b=33
# c=550
# if a>b and c>a:
#     print("Both conditions are True")

# if a>b or a>c:
#     print("at least one of the conditions is True")

#https://www.w3schools.com/python/python_conditions.asp