class Mahsulot:

    def __init__(self, nom, miqdor, narx):
        self.__nom = nom
        self.__miqdor = miqdor
        self.__narx = narx

    def narxni_qaytar(self, soni):
        umumiy = soni * self.__narx
        if soni >= 10:
            umumiy *= 0.9
        return umumiy

    def sotuvni_bajar(self, soni):
        if soni <= self.__miqdor:
            self.__miqdor -= soni
        else:
            print(f"Omborda faqat {self.__miqdor} dona mavjud!")
            self.__miqdor = 0

    def get_nom(self):
        return self.__nom

    def get_miqdor(self):
        return self.__miqdor



m1 = Mahsulot("Shokolad", 120, 10000)
m2 = Mahsulot("Sharbat", 80, 15000)
m3 = Mahsulot("Non", 200, 3000)

mahsulotlar = [m1, m2, m3]

for mahsulot in mahsulotlar:
    print(f"\nMahsulot: {mahsulot.get_nom()}")
    soni = int(input(f"Nechta '{mahsulot.get_nom()}' sotib olmoqchisiz? "))

    umumiy_narx = mahsulot.narxni_qaytar(soni)
    mahsulot.sotuvni_bajar(soni)

    print(f"📦 Mahsulot: {mahsulot.get_nom()}")
    print(f"🧾 Sotilayotgan soni: {soni} dona")
    print(f"💰 Umumiy chegirmali narx: {int(umumiy_narx)} so‘m")
    print(f"📦 Omborda qolgan soni: {mahsulot.get_miqdor()} dona")

