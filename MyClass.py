#OOP
#VD
class NewClass:
    x=5
p1 = NewClass()
print(p1.x)
#VD
class Classmate:
    boy=5
    girl=3
p2 = Classmate()
print(str(p2.boy) + " boys and "+str(p2.girl) +" girls")
#VD
#Function _init_()

class PersonA:
    def __init__(self,name="Wyatt",age=23):
        self.name = name 
        self.age =age

p1 = PersonA("Jog",36)

print(p1.name)
print(p1.age)

p2 = PersonA()

print(p2.name)
print(p2.age)

#VD
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello, my name is "+self.name)
        print("I'm "+str(self.age)+ " years old")

p1 = Person("Wyatt",25)
p1.myfunc()


class PersonB:
    def __init__(self,name,age):
        self.name =name 
        self.age =age
    def myfunc(self):
        print("Hello, my name is "+self.name)
    p1 = Person("John",36)
    p1.age =40
    p1.name= "Leee"
    print(p1.name)
    print(p1.age)

#Delete properties
# del p1.age
#Delete oject
#del p1


