f = open("text.txt","a")
#1
# print(f.read())
#2
#print(f.read(5))
#3
# print(f.readline())
#4
# for x in f:
#     print(x)
#WRITE /CREATE
#GHI VAO CUOI FILE
f.write("now the file has one more line ")
f = open("text.txt","r")
for x in f:
    print(x)
#GHI DE FILE
f = open("text.txt","w")
f.write("One")

#Delete a file
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("Done")
else:
    print("The file does not exist")    

