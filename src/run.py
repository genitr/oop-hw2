from core import Student, Lecturer, Reviewer, add_courses, group_overage_grade

courses = ['Python', 'Git', 'Sql']

student1 = Student('Сергей', 'Есенин', 'М')
add_courses(student1.courses_in_progress, *courses)
student2 = Student('Иван', 'Бунин', 'М')
add_courses(student2.courses_in_progress, *courses)
student3 = Student('Анна', 'Ахматова', 'Ж')
add_courses(student3.courses_in_progress, *courses)

lecturer1 = Lecturer('Максим', 'Горький')
add_courses(lecturer1.courses_attached, courses[0])
lecturer2 = Lecturer('Михаил', 'Лермонтов')
add_courses(lecturer2.courses_attached, courses[1])
lecturer3 = Lecturer('Марк', 'Твен')
add_courses(lecturer3.courses_attached, courses[2])

reviewer1 = Reviewer('Лев', 'Толстой')
add_courses(reviewer1.courses_attached, *courses)
reviewer2 = Reviewer('Александр', 'Пушкин')
add_courses(reviewer2.courses_attached, *courses)

student_group = [student1, student2, student3]
lecturers_group = [lecturer1, lecturer2, lecturer3]

student1.rate_lecturer(lecturer1, courses[0], 9)
student1.rate_lecturer(lecturer2, courses[1], 9)
student1.rate_lecturer(lecturer3, courses[2], 8)

student2.rate_lecturer(lecturer1, courses[0], 10)
student2.rate_lecturer(lecturer2, courses[1], 9)
student2.rate_lecturer(lecturer3, courses[2], 9)

student3.rate_lecturer(lecturer1, courses[0], 9)
student3.rate_lecturer(lecturer2, courses[1], 9)
student3.rate_lecturer(lecturer3, courses[2], 8)

reviewer1.rate_hw(student1, courses[0], 10)
reviewer1.rate_hw(student1, courses[1], 8)
reviewer1.rate_hw(student1, courses[2], 9)

reviewer1.rate_hw(student2, courses[0], 10)
reviewer1.rate_hw(student2, courses[1], 10)
reviewer1.rate_hw(student2, courses[2], 10)

reviewer1.rate_hw(student3, courses[0], 10)
reviewer1.rate_hw(student3, courses[1], 8)
reviewer1.rate_hw(student3, courses[2], 9)

reviewer2.rate_hw(student1, courses[0], 10)
reviewer2.rate_hw(student1, courses[1], 8)
reviewer2.rate_hw(student1, courses[2], 9)

reviewer2.rate_hw(student2, courses[0], 9)
reviewer2.rate_hw(student2, courses[1], 9)
reviewer2.rate_hw(student2, courses[2], 9)

reviewer2.rate_hw(student3, courses[0], 10)
reviewer2.rate_hw(student3, courses[1], 8)
reviewer2.rate_hw(student3, courses[2], 9)

if __name__ == '__main__':
    print('=== Студенты ===')
    print(student1)
    print(student2)
    print(student3)
    print('=== Лекторы ===')
    print(lecturer1)
    print(lecturer2)
    print(lecturer3)
    print('=== Эксперты ===')
    print(reviewer1)
    print(reviewer2)
    print('=== Проверка на равенстово ===')
    print(f'Равен ли student1 и student2 ? \n {student1 == student2}')
    print(f'Равен ли student1 и student3 ? \n {student1 == student3}')
    print(f'Равен ли lector1 и lector2 ? \n {lecturer1 == lecturer2}')
    print(f'Равен ли lector2 и lector3 ? \n {lecturer2 == lecturer3}')
    print('=== Средняя оценка за домашние задания по всем студентам в рамках конкретного курса ===')
    print(f'Python = {group_overage_grade(courses[0], *student_group)}')
    print(f'Git = {group_overage_grade(courses[1], *student_group)}')
    print(f'Sql = {group_overage_grade(courses[2], *student_group)}')
    print('=== Средняя оценка за лекции всех лекторов в рамках курса ===')
    print(f'Python = {group_overage_grade(courses[0], *lecturers_group)}')
    print(f'Git = {group_overage_grade(courses[1], *lecturers_group)}')
    print(f'Sql = {group_overage_grade(courses[2], *lecturers_group)}')
