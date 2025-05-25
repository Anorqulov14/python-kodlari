
# char arr massiv xali otilmaganligi uchun chat gpt yordamida qilindi

def raqam_soz(son):
    birlik = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
    onlik = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
    yuzlik = ["", "bir yuz", "ikki yuz", "uch yuz", "to'rt yuz", "besh yuz", "olti yuz", "yetti yuz", "sakkiz yuz", "to'qqiz yuz"]

    if son > 999:
        return "Ilojsiz"

    yuz = son // 100
    on = (son // 10) % 10
    bir = son % 10

    natija = f"{yuzlik[yuz]} {onlik[on]} {birlik[bir]}".strip()
    return natija.capitalize()

n = int(input("Son kiriting: "))

yigindi = 0
for i in range(1, n + 1):
    if n % i == 0:
        yigindi += i
print(raqam_soz(yigindi))