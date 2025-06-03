def birxil_harflar(lst1,lst2):
    count = 0
    for i,j in zip(lst1,lst2):
        if i.lower() == j.lower():
            count += 1
    return count



print(birxil_harflar("Eldor","elyor"))