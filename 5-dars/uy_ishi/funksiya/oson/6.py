def musbat(lst):
    lists = []
    for i in lst:
        if i >= 0:
            lists.append(i)
    return lists
print(musbat([1, -1, 2, 9, -3, -11, 20, 5, -8, 4]))