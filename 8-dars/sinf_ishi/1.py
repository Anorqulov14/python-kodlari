class Person:

    def __init__(self,nomi,manzil):
        self.__name = nomi
        self.__address = manzil
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def set_address(self,new_address):
        self.__address = new_address
    def __str__(self):
        return f"{self.__name} ({self.__address})"

class Student(Person):
    def __init__(self,nomi,manzil,courses : list[str]=[], grades : list[int]=[]):
        super().__init__(nomi,manzil)
        self.courses = courses
        self.grades = grades
    def add_course_grade(self,course: str, grade: int):
        self.courses.append(course)
        self.grades.append(grade)
    def print_grades(self):
        for self.courses,self.grades in zip(self.courses,self.grades) :
            print(f"kurslar {self.courses} baxolar {self.grades}")
    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)
    def __str__(self):
        return f"Student: {self.get_name()}({self.get_address()})"

class Teacher(Person):
    def __init__(self,nomi,manzil,courses = []):
        super().__init__(nomi,manzil)
        self.courses:list = courses
    def add_course(self,course: str):
        self.courses.append(course)
    def remove_course(self,course: str):
        for k in self.courses:
            if k != course:
                return "Bunday kurs yo'q"
    def __str__(self):
        return f"Teacher: {self.get_name()}({self.get_address()})"
    

s1 = Student("Ali", "Tashkent")
s1.add_course_grade("Math", 90)
s1.add_course_grade("English", 80)

print(s1)  # Student: Ali(Tashkent)
s1.print_grades()
print("O'rtacha baho:", s1.get_average_grade())

t1 = Teacher("Gulbahor", "Samarqand")
t1.add_course("Math")
t1.add_course("Physics")
t1.remove_course("Math")

print(t1)  # Teacher: Gulbahor(Samarqand)
        