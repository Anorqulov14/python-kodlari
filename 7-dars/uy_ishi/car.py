class Car:

    def __init__(self,tezlik,vaqt):
        self.__speed = tezlik
        self.__time = vaqt
    def get_tezlik(self):
        return self.__speed
    def get_vaqt(self):
        return self.__time  
    def get_info(self):
        return self.__speed * self.__time


mashina = Car(60,2)
print(mashina.get_info())