try:
    print(x)
except:
    print("An exception occurred")

print("+++++++++++++++++++++++++")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Sth else went wrong")

print("+++++++++++++++++++++++++")
try:
    print("Hello")
except:
    print("Sth went wrong")
else:
    print("Nothing went wrong")

print("+++++++++++++++++++++++++")
try:
    print(x)
except:
    print("Sth went wrong")
finally:
    print("The try except is finished")  

print("+++++++++++++++++++++++++")
try:
    f = open("demofile.txt")
    f = write("Lorum Ipsum")
except:
    print("Sth went wrong when writing the file")
finally:
    f.close()        
