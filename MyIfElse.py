

# #PYthon If Else
# a=33
# b=200
# if b>a :
#     print("b is great than a")

# # Elif  
# a=39
# b=39
# if b>a:
#     print("b is greater than a")
# elif a>b:
#     print("a is greater than b")
# else:
#   print("a and b are equal")


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



# ##If Else short hand NOT WORK
# a = 2
# b = 330
# print("A") if a > b else print("B")

##NOT WORK
# a=330
# b=330
# print("A") if a>b else print("=") if a==b else print("B")

# a=200
# b=33
# c=550
# if ((a>b) and (c>a)):
#     print("Both conditions are True")
# if (a>b) and (c>a):
#     print("Both conditions are True")
# if ((a>b) and (c>a)):
#     print("Both conditions are True")

a=200
b=33
c=550
if a>b or a>c:
    print("at least one of the conditions is True")