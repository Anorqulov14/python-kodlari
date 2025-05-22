son = int(input("son kiriting: "))
if son >= 80 and son <= 100:
    print("5")
elif son >= 60 and son <= 79:
    print("4")
elif son >= 40 and son <= 59:
    print("3")
elif son >= 20 and son <= 39:
    print("2")
elif son >= 0 and son <= 19:
    print(f"1 Siz bebahosiz")
else:
    print("baxo katta")