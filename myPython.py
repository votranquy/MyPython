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



# #LIST []
# thislist = ["apple","banana","Cherry"] #['apple', 'banana', 'Cherry']
# print(thislist)
# print(thislist[1]) #banana
# thislist[1]="orange" #Change the second item
# print(thislist)
# for x in thislist:
#     print(x)     #apple  orange  Cherry

# thislist = ["apple","banana","cherry"]
# if "apple" in thislist:
#     print("Yes, apple is in this list")
# if "mango" not in thislist:
#     print("Mango is not in thislist")

# #len() get the length of list[] 
# thislist = ["apple","banana","cherry"]
# print("Do dai cua thislist la:") 
# print(len(thislist)) #3   
# #print(thislist)#['apple', 'banana', 'cherry', 'orange']

# #insert(): insert at a special position
# thislist = ["apple","banana","cherry"]
# thislist.insert(1,"orange")#the position 1 is orange
# print(thislist) #['apple', 'orange', 'banana', 'cherry']


# ##remove()
# thislist = ["apple","banana","cherry"]
# thislist.remove("banana")#['apple', 'cherry']
# print(thislist)  


# #pop()
# thislist = ["apple","banana","cherry"]
# thislist.pop() #remove the last
# print(thislist)
# thislist.pop(0) #remove the position 0
# print(thislist)

# #del keyword
# thislist = ["apple","banana","cherry"]
# del thislist[0] #thislist.pop(0)
# print(thislist) #['banana', 'cherry']
# del thislist[0] #thislist.pop(0)
# print(thislist) #['cherry']
# del thislist #Delete completely a list
# #print(thislist) #Error. List is not define
# thislist = ["apple","banana","cherry"]
# del thislist

# clear() :empty a list NOT WORK
# thislist = ["apple","banana","cherry"]
# thislist.clear()
# print(thislist)
# thislist.append("SamSung")
# print(thislist)


# #copy(): NOT WORK
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# ##list(): WORK
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


# # list(())
# thislist =list(("apple","banana","cherry"))
# print(thislist) #['apple', 'banana', 'cherry']
# print(thislist.count("apple"))
# thislist2 = ["kakao","kiwi"]
# thislist.extend(thislist2) #connect 2 lists
# print(thislist)
# print(thislist.index("kakao"))
# thislist.reverse()  #dao nguoc
# print(thislist)
# thislist.sort()
# print(thislist) # sort by ABC



# ##TUPLE
# thistuple = ("Car", "House", "Love")
# print(thistuple) #('Car', 'House', 'Love')

# thislist = ["Car", "House", "Love"]
# print(thislist)
# thistuple = ("Car", "House", "Love")
# print(thistuple)
# print(thistuple[1])

# ERROR when change the value of tuple
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
# del thistuple



# #tuple constructor
# thistuple = tuple(("apple", "samsung","nokia"))
# print(thistuple)
# print(thistuple.count("apple"))#1
# print(thistuple.index("nokia"))#2





# #SETS {}
# thisset={"apple","banana","cherry"}
# print(thisset) #set(['cherry', 'banana', 'apple'])


# thisset={"apple","banana","cherry"}
# for x in thisset:
#     print(x)


# thisset = {'apple','banana', 'cherry'}
# print("banana" in thisset)



# #Can not change the items in set
# #But Can add new items



# thisset = {'apple',"banana",'cherry'}
# thisset.add("orange")
# print(thisset) #set(['orange', 'cherry', 'banana', 'apple'])


# # update() #add some new items
# thisset ={'apple','banana','cherry'}
# thisset.update(['startfruit','dragonfruit','orange'])
# print(thisset) #set(['startfruit', 'apple', 'cherry', 'dragonfruit', 'orange', 'banana'])


# #len()
# thisset = {'apple','mango'}
# print(len(thisset))


##remove()   discard
# thisset = {'apple','mango'}
# thisset.remove('mango')
# print(thisset) #set(['apple'])
# thisset = {'apple','mango'}
# thisset.discard("apple")
# print(thisset) #set(['mango'])


# #pop()
# thisset = {'apple','banana','cherry'}
# x = thisset.pop()
# print(x) #cherry
# print(thisset) #set(['banana', 'apple'])


# # clear() : empty set
# thisset ={'apple',"mango"}
# thisset.clear()
# print(thisset) #set([])



##completely delete a set
# thisset = {"apple","mango"}
# del thisset
# print(thisset) #ERROR


# thisset = set(("apple","banana","cherry"))
# print(thisset)
# #https://www.w3schools.com/python/python_sets.asp



# thistuple = {"apple", "banana", "cherry"}
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")





#https://www.w3schools.com/python/python_conditions.asp