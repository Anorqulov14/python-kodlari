gap = input("soz kiriting: ")

tartib = gap.split()
tori = sorted(tartib,key=str.lower)
print(" ".join(tori))