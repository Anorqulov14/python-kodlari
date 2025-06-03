def eng_katta(l,n):
    lst = []
    for i in l:
        if i < n:
            lst.append(i)
    print(max(lst))
            
eng_katta([1,6,3,9,11],8)