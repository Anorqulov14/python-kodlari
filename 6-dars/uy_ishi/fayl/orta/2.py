file = open("ildiz.txt","w")
talabalar = [16,36,25,49,81]
for i in talabalar:
    ildiz = i ** 0.5
    file.write(str(int(ildiz))+" ")
