son = int(input("son kiriting: "))
y = 0
while son > 0:
    y += son % 10
    son //= 10
print(y)