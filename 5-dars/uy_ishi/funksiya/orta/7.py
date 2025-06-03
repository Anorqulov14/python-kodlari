def kabisa_yilimi(yil):
    lis = []
    for i in yil: 
        i = i % 4 == 0 and i % 100 != 0 or i % 400 == 0
        lis.append(i)
    return lis


print(kabisa_yilimi([1900, 2000, 2016, 1987]))