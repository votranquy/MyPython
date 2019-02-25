print("Hello world")
#Use a Tad to mark a block of code
if 5 > 2:
    print("Of course, 5>2")
#creating a Variable
x = 5
y = "John"
print(x)
print(y)
#change type. It's easy
x = 4
x = "Sally"
print(x)
#Variable
#1. Start with _ (underscore) or letter NOT number
#2. Only contain alpha-numeric character and underscore (A-z, 0-9, _)
#3. Case-sensitive (age and Age are different)
x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x +y
print(z)

x = 5
y = 10
print(x + y)

#Can not use "+" to combine variables being deferent type
# x = 5
# y = "John"
# print(x + y)
# Error

#PYTHON NUMBER
# have int, float, complex
x = 1 #int
y = 2.8 #float
z = 1j+5 #complex
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#INT
x = 2
y = 234834530
z = -1939939
print(type(x))
print(type(y))
print(type(z))
#FLOAT
x = 1.1
y = 1.0
z = -19.39939
print(type(x))
print(type(y))
print(type(z))
x =35e4
y= 12E5
z = -34E2
print(type(x))
print(type(y))
print(type(z))
#COMPLEX
x = 3+5j
y = 5j
z = -34j
print(type(x))
print(type(y))
print(type(z))

x = int(1)
y = int(-1.9)
z = int("3")
print(x)
print(y)
print(z)

x = float(1)
y = float(2.5)
z = float("4")
w = float("5.7")

x = str("s1")
y = str(3)
z = str(3.7)

a = "Heello"
print(a[0]) #Begin from 0
print(a[0:2]) #Get from 0 to 1 (2-1)

a="    Hello   you   "
print(a)
print(a.strip()) #No have space at begining and ending