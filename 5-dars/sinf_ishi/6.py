def listlar(lst) -> list:
    list2 = []
    for i in lst:
        if i > 0:
            list2.append(i)
    return list2


print(listlar(lst = [1, -1, 2, 9, -3, -11, 20, 5, -8, 4]))