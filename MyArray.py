#Use list =Array

#Creat Array
cars =["Ford","Volve","BMW"]
print("List of car:")
print(cars)
print("The first car:")
x=cars[0]
print(x)
print("Change the first car:")
cars[0]="Toyota"
print(cars)
print("The length of car list:")
print(len(cars))

print("The car list:")
x=1
for y in cars:
    print(x,y)
    x+=1 

print("Add the new car:")
cars.append("Honda")
print(cars)

print("remove a car with index")
cars.pop(1) #index 1
print(cars)

print("remove a car with name:")
cars.remove("BMW")#remove the Volve #Ko co xe do thi bi loi
print(cars)

#Array Method
 #append() : add new items to the and of list
numbers=["1","2","3"]
numbers.append("4")
print(numbers)