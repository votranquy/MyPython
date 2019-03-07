def isDoiXung(m):
    tong = 0
    tg = m
    while(tg>0):
        sodu=tg%10
        tong = tong *10 +sodu
        tg=tg//10#Chu y la co 2 dau //
       # print(sodu,tong,tg)
    if tong==m:
        print("OK")
    else:
        print("nOK")       
isDoiXung(7)