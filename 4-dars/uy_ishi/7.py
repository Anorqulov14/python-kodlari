dic = {}
son = int(input("Nechta maxsulot kiritasiz: "))
while son != 0:
    maxsulot = input("Maxsulot kiritasiz: ")
    narxi = input(f"{maxsulot} narxini: ")
    dic.update({maxsulot:narxi})
    son -= 1

print(dic)
