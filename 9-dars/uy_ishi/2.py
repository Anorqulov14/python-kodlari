class Cinema:
    def __init__(self,id,name):
        self.id = id
        self.__name = name
        self.movies = {}
        self.income = {}
    def getName(self):
        return self.__name
    def addMovie(self,movie : str,seats : int):
        self.movie = movie
        self.seats = seats
        for kino in self.movies:
            if kino == movie:
                kino[seats]+=seats
            else:
                self.kino