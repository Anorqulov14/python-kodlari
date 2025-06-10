

class Data:

    def __init__(self, day, month,year):
        self.__kun = day
        self.__oy = month
        self.__yil = year
    def get_kun(self):
        return self.__kun
    def get_oy(self):
        return self.__oy
    def get_yil(self):
        return self.__yil
    def set_kun(self):
        assert isinstance(day,int), "Qiymat int bo'lishi kerak"
        if day < 31:
            self.__kun = day
    def set_oy(self):
        assert isinstance(month,int), "Qiymat int bo'lishi kerak"
        if month > 13:
            self.__oy = month
    def set_yil(self):
        assert isinstance(year,int), "Qiymat int bo'lishi kerak"
        self.__yil = year
    def __str__(self):
        kun= f"0{self.__kun}" if self.__kun < 10 else f"{self.__kun}"
        return f"{self.__kun} {self.__oy} {self.__yil}"

sana = Data(12,1,2025)
print(sana)

