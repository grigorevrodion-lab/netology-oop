class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.average_grade()
        return f"{super().__str__()}\nСредняя оценка за лекции: {avg_grade:.1f}"

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов")
        return self.average_grade() >= other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course not in student.grades:
                student.grades[course] = []
            student.grades[course].append(grade)
        else:
            return "Ошибка"

    def __str__(self):
        return f"{super().__str__()}"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
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
        avg_grade = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов")
        return self.average_grade() >= other.average_grade()


# Тестирование реализации
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Пётр', 'Петров')
reviewer = Reviewer('Сергей', 'Сергеев')
student1 = Student('Алёхина', 'Ольга', 'Ж')
student2 = Student('Иванов', 'Алексей', 'М')

# Назначение курсов
student1.courses_in_progress += ['Python', 'Java']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python', 'C++']
student2.finished_courses += ['Введение в программирование']

lecturer1.courses_attached += ['Python', 'Java']
lecturer2.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'Java']

# Выставление оценок
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Java', 8)
student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'C++', 9)

reviewer.rate_hw(student1, 'Python', 9)
reviewer.rate_hw(student1, 'Java', 8)
reviewer.rate_hw(student2, 'Python', 10)
reviewer.rate_hw(student2, 'C++', 9)

# Тестирование магических методов __str__
print("=== ЛЕКТОР ===")
print(lecturer1)
print("\n=== ПРОВЕРЯЮЩИЙ ===")
print(reviewer)
print("\n=== СТУДЕНТ ===")
print(student1)

# Тестирование сравнения
print("\n=== СРАВНЕНИЕ ЛЕКТОРОВ ===")
print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")
print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")
print(f"Лектор1 == Лектор2: {lecturer1 == lecturer2}")

print("\n=== СРАВНЕНИЕ СТУДЕНТОВ ===")
print(f"Студент1 > Студент2: {student1 > student2}")
print(f"Студент1 < Студент2: {student1 < student2}")
print(f"Студент1 == Студент2: {student1 == student2}")
