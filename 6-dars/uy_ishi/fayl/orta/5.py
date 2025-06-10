print("1, 2 yoki 3 ni tanlang\n")
print("\t1. Yangi fayl yarating")
print("\t2. Faylni ko'rsatish")
print("\t3. Faylga yangi element qo'shish")

tanlov = input("Tanlovingizni kiriting (1/2/3): ")

if tanlov == "1":
    fan = input("Maktab fanini kiriting: ")
    with open("fan.txt", "w", encoding="utf-8") as f:
        f.write(fan + "\n")
    print("Fayl yaratildi va fan saqlandi.")

elif tanlov == "2":
    try:
        with open("fan.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print("Fayl tarkibi:")
            print(content)
    except FileNotFoundError:
        print("Xatolik: 'fan.txt' fayli topilmadi.")

elif tanlov == "3":
    try:
        yangi_fan = input("Yangi fan kiriting: ")
        with open("fan.txt", "a", encoding="utf-8") as f:
            f.write(yangi_fan + "\n")
        print("Fan qo‘shildi.\nYangi fayl tarkibi:")
        with open("fan.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Xatolik: 'fan.txt' fayli hali mavjud emas. Avval 1-variantni tanlang.")

else:
    print("❌ Noto‘g‘ri tanlov. Faqat 1, 2 yoki 3 ni kiriting.")
