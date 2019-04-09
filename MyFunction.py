
# #Function
# #VD

# #Tao ham
# def my_function():
#     print("This is a function")
# #Goi ham
# my_function()


# #Tham so trong ham
# #VD
# def myfunction1(name):
#     print(name + "is your friend")
# myfunction1("Emil")
# myfunction1("Beta")


# #Tham so mac dinh
# #VD
# def secondfunction(country="Vietnam"):
#     print("The country is " + country)
# secondfunction()
# secondfunction("Cambodia")
# secondfunction("Laos")



# #VD
# def luythuabac2(x):
#   return x*x
# print(luythuabac2(5))
# print(luythuabac2(10))



# #DE QUI
# def tri_recursion(k):
#     if(k>0):
#         result = k + tri_recursion(k-1)
#         #return(result)
#     else:
#         result=0
#     return result
# print("Ket qua dung de qui: ")
# tri_recursion(6)
# #6+5+4+3+2+1+0
# # kq = 6 + 5 + 4 +3 +2 +1 
# print("\n\nThe result is:")
# print(6+5+4+3+2+1+0)



# def addten(a):
#   return a+10
# #Lambda function
# print("Lambda function")
# x= lambda a:a+10
# print(x(5))
# print(addten(5))
# y = lambda a, b : a*b 
# print(y(5,4))
# z = lambda a, b, c : a*b*c 
# print(z(1,2,3))



# x =lambda a,b :a*b 
# print(x(5,6))

# x= lambda a,b,c: a+b*c 
# print(x(1,2,3))


# #Dang ap dung cua lambda
# def myfunc(n):
#     return lambda a: a*n 
# mydoubler= myfunc(2)
# print(mydoubler(11))


# def myfunc(n):
#     return lambda a: a*n
# mytripler = myfunc(3)
# mydouble = myfunc(2)
# print(mytripler(11))
# print(mydouble(10))