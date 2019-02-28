# 2 types of loop

# while and for

#1. While
i=1
while i<6:
    print(i)
    i+=1

#break 
i=1
while i<6:
    print(i)
    if i==3: break
    i+=1
#continue
i=0
while i<6:
    i+=1
    if i==3: continue
    print(i)

#For loop
 #use for list, tuple, dictionary, set, string
#VD
fruits =["apple","banana","orange"]
for x in fruits:
    print(x)
#VD
for x in "banana":
    print(x)
#VD
fruits =["apple","banana","cherry","orange"]
for x in fruits:
    print(x)
    if x=="banana": break
#VD
fuits =["apple","banana","cherry"]
for x in fruits:
    if x=="banana": break
    print(x)
#VD
fruits =["apple","banana","cherry"]
for x in fruits:
    if x=="banana": continue
    print(x)
#VD
print("++++++++++++")
fruits =["banana","apple"]
for x in fruits:
    if x=="banana": continue
    print(x)
# range()
#VD
print("++++++++++++")
for x in range(6):
    print(x)#in tu 0 den 5
#VD    
print("++++++++++++") 
for x in range(4,7):
    print(x)   
#VD
print("++++++++++++") 

for x in range(19,1,-3):
    print(x)
#else in For
print("++++++++++++") 
for x in range(6):
    print(x)
else: 
    print("Finally finished!")
#Lap long nhau
adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits: print(x,y)


#Function
#VD
    #Tao ham
def my_function():
    print("this is a function")
    #GOi ham
my_function()
#Tham so trong ham
#VD
def myfunction1(name):
    print(name + "is your friend")
myfunction1("EMil")
myfunction1("BETA")
#Tham so mac dinh
#VD
def secondfunction(country="VIetnam"):
    print("The country is " + country)
secondfunction()
secondfunction("Cambodia")
secondfunction("Laos")

#VD
def luythuabac2(x):
    return x*x
print(luythuabac2(5))
print(luythuabac2(10))  
#DE QUI
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result
tri_recursion(6)
#6+5+4+3+2+1+0
# kq = 6 + 5 + 4 +3 +2 +1 
print("\n\nThe result is:")
print(6+5+4+3+2+1+0)
#Lambda function
print("Lambda function")
x= lambda a:a+10
print(x(5))


x =lambda a,b :a*b 
print(x(5,6))

x= lambda a,b,c: a+b*c 
print(x(1,2,3))


#Dang ap dung cua lambda
def myfunc(n):
    return lambda a: a*n 
mydoubler= myfunc(2)
print(mydoubler(11))


def myfunc(n):
    return lambda a: a*n
mytripler = myfunc(3)
mydouble = myfunc(2)
print(mytripler(11))
print(mydouble(10))
