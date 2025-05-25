for k in range(1, 11, 5):
    for j in range(1, 11):
        for i in range(k, k + 5):
            if i <= 10:
                print(f"{i:2} * {j:2} = {i*j:3}", end="   ")
        print()
    print()




