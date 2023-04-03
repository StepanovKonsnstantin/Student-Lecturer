class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def av_rating(self):
        rating = 0
        for x in self.grades.values():
            rating = float(sum(x) / len(x))
        return rating

    def __str__(self):
        d = ','
        res = f'Имя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.av_rating()}\nКурсы в процессе изучения: {d.join(self.courses_in_progress)}\nЗавершенные курсы: {d.join(self.finished_courses)}'
        return res

    # def average_rating_student_course(a, b):
    # rating = 0
    # for x in a:
    #     for y in x.grades.get(b):
    #         rating = float(sum(y)/len(y))
    # return rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        # self.grades = {}

    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname, ):
        super().__init__(name, surname)
        self.grades = {}

    def av_rating(self):
        rating = 0
        for x in self.grades.values():
            rating = float(sum(x) / len(x))
        return rating

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.av_rating()} '
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.av_rating() < other.av_rating()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия: {self.surname}'
        return res


def average_rating_student_course(a, b):
    s_rating = 0
    p_rating = 0
    result = 0
    for x in a:
        for y in x.grades.get(b):
            s_rating += y
            p_rating += 1
    return print(f'Средняя оценка по всем студентам в рамках курса {b}:{float(s_rating/p_rating)}')

def average_rating_lecturer_course(a, b):
    s_rating = 0
    p_rating = 0
    for x in a:
        for y in x.grades.get(b):
            s_rating += y
            p_rating += 1
    return print(f'Средняя оценка по всем лекторам в рамках курса {b}:{float(s_rating/p_rating)}')


student_1 = Student('Джо', 'Абама', 'муж.')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['VB']
student_1.finished_courses += ['C++']

student_2 = Student('Вероника', 'Степанова', 'жен.')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['C++']
student_2.finished_courses += ['VB']

reviewer_1 = Reviewer('Александр', 'Петров')
reviewer_1.courses_attached += ['VB']
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Николай', 'Пономарев')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['C++']

lecturer_1 = Lecturer('Александр', 'Строгий')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['VB']

lecturer_2 = Lecturer('Иван', 'Добрый')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['C++']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_1, 'VB', 9)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'C++', 10)

student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'VB', 9)
student_1.rate_hw(lecturer_1, 'Python', 8)

student_2.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'VB', 8)
student_2.rate_hw(lecturer_2, 'Python', 9)

print(student_1)

print(reviewer_1)

print(lecturer_1)

print(student_1 > lecturer_1)

average_rating_student_course([student_1, student_2], 'Python')

average_rating_lecturer_course([lecturer_1, lecturer_2], 'Python')