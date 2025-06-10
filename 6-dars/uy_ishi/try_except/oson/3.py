try: 
    son1 = int(input("1 son kiriting: "))
    son2 = int(input("2 son kiritng: "))
    print(son1/son2)
except ValueError:
    print("Raqam kiriting")
except ZeroDivisionError:
    print("0 ga bolish mumkin emas")
