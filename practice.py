# Use plus to combine two variables with same type
x = "awesome"
print("Puthon is "+ x)

#Work Ok because x and y are same type
x = 5
y = 7
print(x+y)

#Work error because x and y are different type
# x = 5
# y = "ABC"
# print(x+y)

#With if condition, the function at the new line must have a tab
if 5 > 3:
  print("It works")

#Without tab, it doesn't work
# if 5>3:
# print("Not work")


#=================================
#3 types of number in Python
# type in
x = 1
print(type(x)) #<type 'int'>

#type float
x = -1.45
print(type(x)) #<type 'float'>

#type complex
x = 3 + 5j
print(type(x)) #<type 'complex'>

#=================================

#Python Casting: Use to spedifine or change the type of one variable
#int
x = int (1) #int to int
y = int(2.8)#float to int #2
z= int("3") #string to int #3
print(x)
print(y)
print(z)

#float
x = float(1)#int to float #1.0
y = float(2.8)# float to float #2.8
z = float("390") #string to float #390.0
w = float("4.3") #string to flaot #4.3
print(x)
print(y)
print(z)
print(w)

#string
x = str("s1234")# str to str  #s1234
y = str(2) #int to float      #2
z = str(3.0) #float to string #3.0
print(x)
print(y)
print(z)

#=================================
#String
a = "Helloooo ABC"
#Print the letter at one position
print(a[0])
print(a[1]) #Print the letter at 2nd position
print(type(a))#<type 'str'>
print(type(a[1]))#<type 'str'>
#Print the substring from A position to B one position
#Remember it only print from A to < B, not include B
print(a[2:5]) #Remember [2:5) #llo

#strip() method: remove the white space at the beginning and ending
a = "    ABC   "
a = a.strip() #"ABC"
b = "Test"
print(b+a+b) #TestABCTest

#len() method: print the length of a str(inclue whitespace)
a = " ABC ABC " #9
print(len(a))

#lower() : lower case the string

a = "Hello WoRLd"
print(a.lower()) #hello world

#upper(): upper case the string

a = "Hello WoRLd"
print(a.upper()) #HELLO WORLD

#replace(): replace("A","B") replace a tring with another string

a = "Hello, World"
print(a.replace("Hello","HELLOA"))

#split(): split the string into substr by boundation
a = "Hello, World,ABC "
print(a.split(","))#['Hello', ' World', 'ABC ']

#Input string by command line

# print("Please enter your name:")
# x = input()
# print("Your name is ", x) #REMEMBER (not use plus here)

print("Enter your name:")
f = input()
print("Hello, ", f)






