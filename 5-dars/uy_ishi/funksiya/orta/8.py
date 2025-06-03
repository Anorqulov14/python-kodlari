
def kabisa_yilimi(yil):
    lis = []
    for i in yil: 
        i = i % 4 == 0 and i % 100 != 0 or i % 400 == 0
        lis.append(i)
    return lis

def oyda_kun(yil, oy):
    lis2 = []
    for i in oy:
        if i == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            i == 31
            lis2.append(i)
        elif i == 4 or i == 6 or i == 9 or i == 11:
            i == 30
            lis2.append(i)
        if i == 2:
            if kabisa_yilimi(yil) == True:
                i == 29
                lis2.append(i)
            else:
                i == 28
                lis2.append(i)
    return lis2

print(oyda_kun([1900, 2000, 2016, 1987],[2, 2, 1, 11]))
