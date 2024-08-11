"""Модуль содержит оснвную логику программы"""

def overage_grade(grades: dict) -> float:
    """Получение средней оценки"""
    count, summary = 0, 0
    for _, value in grades.items():
        for i in value:
            summary += i
        count += len(value)
    return summary / count

def group_overage_grade(course: str, *group) -> float:
    """Подсчёт средней оченки на курсе среди всех участников"""
    count, summary = 0, 0
    for member in group:
        for key, value in member.grades.items():
            if key == course:
                for i in value:
                    summary += i
                count += len(value)
    return round(summary / count, 1)

def add_courses(instance_course, *courses) -> None:
    """Добавление курсов"""
    for value in courses:
        instance_course.append(value)


class Student:
    """Класс студента"""
    def __init__(self, name: str, surname: str, gender: str) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer: object, course: str, grade: int):
        """Выставление оценки лектору"""
        if (isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
            and self.courses_in_progress):

            if 11 > grade > 0:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Недопустимая оценка! Используйте цифры от 1 до 10'
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        """Перегрузка метода"""
        return (
        f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {round(overage_grade(self.grades), 1)}
        Курсы в процессе изучения: {self.courses_in_progress}
        Завершенные курсы: {self.finished_courses}
        """)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Student):
            return overage_grade(self.grades) == overage_grade(value.grades)


class Mentor:
    """Класс преподователя"""
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс лекторов"""
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self) -> str:
        """Перегрузка метода"""
        return (
        f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {round(overage_grade(self.grades), 1)}
        """)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Lecturer):
            return overage_grade(self.grades) == overage_grade(value.grades)


class Reviewer(Mentor):
    """Класс проверяющих экспертов"""

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

    def __str__(self) -> str:
        """Перегрузка метода"""
        return (
        f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        """)
