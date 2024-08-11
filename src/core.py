"""Модуль содержит оснвную логику программы"""
class Student:
    """Класс студента"""
    def __init__(self, name: str, surname: str, gender: str) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    """Класс преподователя"""
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student: object, course: str, grade: int):
        """Выставление студенту оценки за прохождение курса"""

        if (isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress):

            if 11 > grade > 0:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Недопустимая оценка! Используйте цифры от 1 до 10.'
        else:
            return 'Ошибка'
