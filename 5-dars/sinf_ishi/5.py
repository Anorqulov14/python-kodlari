def boluvchi(n):
    lst = []
    for i in range(2,n):
        if n %i == 0:
            lst.append(i)
    return lst

print(boluvchi(10))
