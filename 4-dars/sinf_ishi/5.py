
login = {
    "jeymsBond": "agent007",
    "tony_stark": "ironman101",
    "piterParker": "spider",
    "sherlok": "sher.l04",
}
log = input("login kiriting: ")
par = input("parol kiriting: ")
for loginlar, parol in login.items():
    if loginlar == log and parol == par:
        print("kirdingiz")
        break
else:
    print("xato")
