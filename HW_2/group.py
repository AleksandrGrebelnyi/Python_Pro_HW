from student_subclass import Student
from person_superclass import Person


class Group:
    group_students = 0

    def __init__(self, course):
        self.course = course
        self.group_students = []

    def add_student(self, student: Student):
        if student not in self.group_students and Student.total_students != 10:
            self.group_students.append(student)
            Student.total_students += 1

    def remove_student(self, student: Student):
        self.group_students.remove(student)
        if self.group_students:
            Student.total_students -= 1

    def find_student(self, lastname,*args, **kwargs):
        for i, item in enumerate(self.group_students):
            if lastname in item.lastname:
                print('\nStudent found: ', self.group_students[i])

    def __str__(self, *args, **kwargs):
        res = f'Course: {self.course}\n'
        res += f'Students group:\n\t{"".join(map(str, self.group_students))}\n'
        res += f'Total: {Student.total_students} students'

        return res