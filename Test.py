#Tạo một mảng ngẫu nhiên (tự sinh ra)
import random
array= []
array1= []
n = random.randint(1,101)
for x in range(n):
    array.append(random.randint(1,101))
print("Da tao mang co so phan tu la: ")
print(n)
print("Mang da tao: ")
print(array)


#Sap xep tang dan bang ham sort()
array1=array
array1.sort()
print("Mang sau khi sap xep tang, dung ham sort:")
print(array1)
array1=sorted(array,reverse= True)
print("Mang sau khi sap xep giam, khong dung ham sort:")
print(array1)

#Ham check so nguyen to
def isNguyenTo(x):
    for i in range(x):
        if i>1 and i<x and x%i==0:
            return("false")
    array2.append(x)
    return("true")

#Dem so nguyen to
dem=0
array2=[]
for y in array:
    if(isNguyenTo(y)=="true"): dem+=1
print("So luong so nguyen to: ")
print(dem)
print("Danh sach so nguyen to la: ")
print(array2)


#Sap xep khong dung ham sort()
array3=array1
n = len(array3)
for x in range(0,n-1):
    for y in range(x+1,n):
        if array3[x]>array3[y]:
            tg=array3[x]
            array3[x]=array3[y]
            array3[y]=tg
print("Ket qua sap xep tang dan khong dung ham sort: ")
print(array3)    

#Nhap so
print("Moi ban nhap mot so:")
s=input()
print("So ban da nhap:")
print(s)

#Ham check so nguyen to
def isNguyenTo(x):
    for i in range(2,x):
        if x%i==0: return('false')
    return("true") 

if(isNguyenTo(int(s))=="true"):
    print("La so nguyen to")
else:
    print("Khong la so nguyen to")

# Ham in ra day so fibonaxy nho hon N
def fibonaxi(n):
    x1 = 1
    x2 = 1
    x3 = 2
    arrayA=[]
    if n>1:
        arrayA.append(x1)
        arrayA.append(x2)
        while(x3<n):
            if x3<n: arrayA.append(x3)
            x1=x2
            x2=x3
            x3=x1+x2 
    return arrayA

n= random.randint(1,101)
arrayB = fibonaxi(n)
print("Day so fibonaxi: ")
print(arrayB)

#Ham kiem tra so chinh phuong
def isChinhPhuong(n):
    i=0
    while(i*i<=n):
        if(i*i==n): return("true")
        i+=1
    return("false")

if(isChinhPhuong(1)=="true"):
    print("La so chinh phuong")
else:
    print("Khong phai so chinh phuong")

#Ham kiem tra mot so doi xung
def isSoDoiXung(n):
    M = 0
    tmp = n
    while(tmp>0):
        k = tmp%10
        M = M*10 + k
        tmp = tmp/10
    print(M) 
    print(n)   
    if M==n: 
        print   
        print("CO") 
    else:
        print("KHONG") 
isSoDoiXung(141)
# if(isSoDoiXung(141) =='true'):
#     print("La so doi xung")
# else:
#     print("Khong phai la so doi xung nha")    

def isDoiXung(m):
    tong = 0
    tg = m
    while(tg>0):
        sodu=tg%10
        tong = tong *10 +sodu
        tg=tg//10
    if tong==m:
        print("OK")
    else:
        print("nOK")
isDoiXung(71)           





