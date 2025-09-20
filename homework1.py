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


# Функции для подсчета средних оценок
def average_student_grade(students, course):
    """
    Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
    """
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])

    if not total_grades:
        return 0

    return sum(total_grades) / len(total_grades)


def average_lecturer_grade(lecturers, course):
    """
    Подсчет средней оценки за лекции всех лекторов в рамках курса
    """
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])

    if not total_grades:
        return 0

    return sum(total_grades) / len(total_grades)


# Создание экземпляров классов
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Пётр', 'Петров')

reviewer1 = Reviewer('Сергей', 'Сергеев')
reviewer2 = Reviewer('Анна', 'Андреева')

student1 = Student('Алёхина', 'Ольга', 'Ж')
student2 = Student('Иванов', 'Алексей', 'М')

# Назначение курсов
student1.courses_in_progress += ['Python', 'Java', 'Git']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python', 'C++', 'Git']
student2.finished_courses += ['Введение в программирование']

lecturer1.courses_attached += ['Python', 'Java']
lecturer2.courses_attached += ['Python', 'C++']

reviewer1.courses_attached += ['Python', 'Java']
reviewer2.courses_attached += ['Python', 'C++', 'Git']

# Выставление оценок студентам
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Java', 7)
reviewer1.rate_hw(student1, 'Java', 9)

reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'C++', 8)
reviewer2.rate_hw(student2, 'C++', 9)
reviewer2.rate_hw(student2, 'Git', 10)

reviewer2.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student1, 'Git', 9)

# Выставление оценок лекторам
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer1, 'Java', 7)
student1.rate_lecture(lecturer1, 'Java', 9)

student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'C++', 8)
student2.rate_lecture(lecturer2, 'C++', 9)

# Тестирование всех методов
print("=== ТЕСТИРОВАНИЕ ВЫВОДА ===")
print("\nЛЕКТОР 1:")
print(lecturer1)
print("\nЛЕКТОР 2:")
print(lecturer2)
print("\nПРОВЕРЯЮЩИЙ 1:")
print(reviewer1)
print("\nПРОВЕРЯЮЩИЙ 2:")
print(reviewer2)
print("\nСТУДЕНТ 1:")
print(student1)
print("\nСТУДЕНТ 2:")
print(student2)

print("\n=== ТЕСТИРОВАНИЕ СРАВНЕНИЯ ===")
print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")
print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")
print(f"Лектор1 == Лектор2: {lecturer1 == lecturer2}")

print(f"Студент1 > Студент2: {student1 > student2}")
print(f"Студент1 < Студент2: {student1 < student2}")
print(f"Студент1 == Студент2: {student1 == student2}")

print("\n=== ТЕСТИРОВАНИЕ ФУНКЦИЙ ДЛЯ ПОДСЧЕТА СРЕДНИХ ОЦЕНОК ===")
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

python_student_avg = average_student_grade(students_list, 'Python')
python_lecturer_avg = average_lecturer_grade(lecturers_list, 'Python')
java_student_avg = average_student_grade(students_list, 'Java')
java_lecturer_avg = average_lecturer_grade(lecturers_list, 'Java')
git_student_avg = average_student_grade(students_list, 'Git')

print(f"Средняя оценка студентов по курсу Python: {python_student_avg:.1f}")
print(f"Средняя оценка лекторов по курсу Python: {python_lecturer_avg:.1f}")
print(f"Средняя оценка студентов по курсу Java: {java_student_avg:.1f}")
print(f"Средняя оценка лекторов по курсу Java: {java_lecturer_avg:.1f}")
print(f"Средняя оценка студентов по курсу Git: {git_student_avg:.1f}")

print("\n=== ПРОВЕРКА ОЦЕНОК В СЛОВАРЯХ ===")
print(f"Оценки студента1: {student1.grades}")
print(f"Оценки студента2: {student2.grades}")
print(f"Оценки лектора1: {lecturer1.grades}")
print(f"Оценки лектора2: {lecturer2.grades}")