class Point:

    def __init__(self,kordinata1,kordinata2):
        self.__x = kordinata1
        self.__y = kordinata2
    def get_kordinata1(self):
        return self.__x
    def get_kordinata2(self):
        return self.__y 
    def get_quarter(self):
        return self.__x + self.__y


point = Point(-3, 5)
print(point.get_quarter())  