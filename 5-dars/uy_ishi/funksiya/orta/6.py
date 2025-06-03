def findall(str1,str2):
    count = 0
    lst = []
    for i in str1.split():
        for j in i:
            if j == 'a':
                count+=1
        lst.append(count)
    
    for k in str2.split():
        count = 0
        for l in k:
            if l == 'a':
                count+=1
        lst.append(count)
    print(lst)       
     


findall("men ,mohir dasturchiman", "mal")