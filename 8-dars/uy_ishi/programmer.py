class Developer:
    def __init__(self, surname, salary, position):
        self.surname = surname
        self.salary = salary
        self.position = position

class SoftwareEngineer(Developer):
    def __init__(self, surname, position, salary, bonus, department):
        super().__init__(surname, salary, position) 
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

departments = {}

for eng in engineers:
    dept = eng.department
    if dept not in departments:
        departments[dept] = {
            "count": 0,
            "total_payment": 0
        }
    departments[dept]["count"] += 1
    departments[dept]["total_payment"] += eng.payment()

for dept in sorted(departments.keys()):
    count = departments[dept]["count"]
    total = departments[dept]["total_payment"]
    print(f"{dept}: {count} ta dasturchi, jami to‘lov: {total}")


