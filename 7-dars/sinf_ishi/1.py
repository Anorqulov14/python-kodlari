class HisobRaqami:

    def __init__(self, ism, balans):
        self.ism = ism
        self.balans = balans

    def pul_tushir(self, pul):
        if pul >= 0:
            self.balans += pul
        else:
            print("xato")

    def pul_yechish(self,pul):
        if self.balans >= pul:
            self.balans -= pul
        else:
            print("xato")

    def ekranga(self):
        print(f"{self.ism} {self.balans}")


odam = HisobRaqami("anvar",500) 
# odam.ekranga()

# odam.pul_tushir(500)
# odam.ekranga()

odam.pul_yechish(600)
odam.ekranga()
