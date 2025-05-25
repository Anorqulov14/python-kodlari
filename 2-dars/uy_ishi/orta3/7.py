def tubmi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True


son = int(input("son kiriting: "))
son1 = int(input("son kiriting: "))

for i in range(son,son1+1):
    if tubmi(i):
        print(i, end=" ") 