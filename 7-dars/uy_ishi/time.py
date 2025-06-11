class Time:

    def __init__(self,soat,minut,sekund):
        self.__hour = soat
        self.__minute = minut
        self.__second = sekund
    def time_left(self):
        a = self.__hour * 3600 + self.__minute * 60 + self.__second
        b = 24 * 3600
        c = b - a

        hours = c // 3600
        c %= 3600
        minutes = c // 60
        seconds = c % 60

        return hours, minutes, seconds
    def add_minutes(self, minutes):
        secondla = self.__hour * 3600 + self.__minute * 60 + self.__second
        secondla += minutes * 60
        secondla %= 24 * 3600 

        hour = secondla // 3600
        secondla %= 3600
        minut = secondla // 60
        second = secondla % 60

        return f"{hour}:{minut}:{second}"
    def __str__(self):
        return f"soat:{self.__hour} minut:{self.__minute} sekund:{self.__second}"


time1 = Time(21, 15, 30)
time2 = Time(22, 45, 0)
time3 = Time(13, 0, 0)
time4 = Time(23, 59, 59)
time5 = Time(0, 0, 0)

objects = [time1, time2, time3, time4, time5]

for t in objects:
    print("Vaqt:", t)
    print("24:00:00 gacha qolgan daqiqa:", t.time_left())
    print("100 daqiqa qo‘shilgandan so‘ng:", t.add_minutes(100))
    print()