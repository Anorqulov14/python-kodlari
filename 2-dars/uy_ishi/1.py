import random


daraja = int(input("""Darjani tanlang:
    1. Oson
    2. O'rta
    3. Qiyin\n"""))

while daraja <= 3 :
    if daraja == 1:
        boshi = 1
        ohiri = 5
    elif daraja == 2:
        boshi = 5
        ohiri = 10
    elif daraja == 3:
        boshi = 10
        ohiri = 15

    count = 0
    xato = 0
    hisobla = 1
    
    for i in range(1,6):
        son = random.randint(boshi,ohiri)
        son1 = random.randint(boshi,ohiri)
        amal = random.choice(["+","-","*","//"])
        if amal == "+":
            natija = son + son1
        elif amal == "-":
            natija = son - son1
        elif amal == "*":
            natija = son * son1
        else:
            natija = son // son1
        fson = int(input(f"{son} {amal} {son1} = "))
        if natija == fson:
            print("tog'ri")
            count+=1
        else:
            print("xato")
            xato +=1 
    if count > xato:
        
        if daraja == 3:
            print("Tabriklayman")
            break
        else:
            daraja += 1
            print("keyingi darajaga otdingiz")
    else:
        print("yutqazdingiz")
        hisobla = 0
        break
