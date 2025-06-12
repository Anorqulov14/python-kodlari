class Developer:

    def __init__(self,surname,salary,position):
        self.surname = surname
        self.salary = salary
        self.position = position

class SoftwareEngineer(Developer):

    def __init__(self,surname,position,salary,bonus,department):
        super().__init__(surname,position,salary)
        self.bonus = bonus
        self.department = department
    def payment(self):
        return self.salary + self.bonus

engineers = [
    SoftwareEngineer("Anvar", "Junior", 500, 100, "1-bo'lim"),
    SoftwareEngineer("Asror", "Middle", 1500, 500, "2-bo'lim"),
    SoftwareEngineer("Kamola", "Senior", 2500, 100, "3-bo'lim"),
    SoftwareEngineer("Vali", "Junior", 500, 100, "1-bo'lim"),
    SoftwareEngineer("Davron", "Middle", 1500, 100, "2-bo'lim"),
]

