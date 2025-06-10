from math import pi



class Aylana:

    def __init__(self, radius, rangi):
        self.__radius = radius
        self.__rangi = rangi

    # o'qish
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__rangi
    # yozish
    def set_radius(self, radius):
        assert isinstance(radius,(int,float)), "Qiymat int yoki float bo'lishi kerak"
        self.__radius = radius

    def set_radius(self, rangi):
        assert isinstance(rangi,str), "Qiymat str bo'lishi kerak"
        self.__rangi = rangi
    # hisobla
    def get_area(self):
        return pi * self.__radius ** 2

    def get_circumference(self):
        return 2 * pi * self.__radius

    def __str__(self):
        return f"{self.__radius} {self.__rangi} radiusi {self._Aylana__get_area()} uzunligi {self.__get_circumference()}"
    
    

aylana1 = Aylana(10, "oq")
aylana1.get_area()

# print(aylana1.rangi)
print(aylana1)
