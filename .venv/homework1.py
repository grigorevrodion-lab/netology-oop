class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"{self.name} {self.surname}"
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для хранения оценок за лекции

    def __str__(self):
        return f"Лектор: {super().__str__()}"

    def average_grade(self, course=None):
        """Расчет средней оценки за лекции"""
        if course:
            if course in self.grades and self.grades[course]:
                return sum(self.grades[course]) / len(self.grades[course])
            return 0
        else:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades) if all_grades else 0


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Выставление оценки студенту за домашнее задание"""
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course not in student.grades:
                student.grades[course] = []
            student.grades[course].append(grade)
        else:
            return "Ошибка"

    def __str__(self):
        return f"Проверяющий: {super().__str__()}"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """Выставление оценки лектору за лекцию"""
        if not isinstance(lecturer, Lecturer):
            print("Ошибка: Можно оценивать только лекторов")
            return "Ошибка"

        if (course not in self.courses_in_progress or
                course not in lecturer.courses_attached):
            print("Ошибка: Курс не найден у студента или лектора")
            return "Ошибка"

        if grade < 1 or grade > 10:
            print("Ошибка: Оценка должна быть от 1 до 10")
            return "Ошибка"

        if course not in lecturer.grades:
            lecturer.grades[course] = []
        lecturer.grades[course].append(grade)

    def __str__(self):
        return f"Студент: {self.name} {self.surname}"

    def average_grade(self, course=None):
        """Расчет средней оценки за домашние задания"""
        if course:
            if course in self.grades and self.grades[course]:
                return sum(self.grades[course]) / len(self.grades[course])
            return 0
        else:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades) if all_grades else 0

# #Creat classes
#
# class Lecturer(Mentor):
#     pass
#
# class Reviewer(Mentor):
#     pass

# Тестирование реализации
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'C++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}
#
# print(isinstance(lecturer, Mentor))  # True
# print(isinstance(reviewer, Mentor))  # True
# print(lecturer.courses_attached)     # []
# print(reviewer.courses_attached)     # []
