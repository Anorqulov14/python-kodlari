
N = int(input("son kiriting: "))


a = 0
b = 1

print("Fibonachchi sonlari:")
for i in range(N):
    print(a)
    a, b = b, a + b
