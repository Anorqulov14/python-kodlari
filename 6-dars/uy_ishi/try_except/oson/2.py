try:
    lst = list(map(int, input("Sonlar: ").split()))
    index = int(input("index kiritng: "))
    print(lst[index])
except IndexError:
    print("Xato")