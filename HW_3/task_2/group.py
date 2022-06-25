from student import Student
from settings import LIMIT_OF_STUDENTS
from exception import GroupLimit


class Group:
    stp = 0

    def __init__(self, course: str):
        self.course = course
        self.group_students = []

    def add_student(self, student: Student):
        if student not in self.group_students and len(self.group_students) >= LIMIT_OF_STUDENTS:
            raise GroupLimit(len(self.group_students), "We can't take more students\n")
        self.group_students.append(student)
        Group.stp += 1

    def remove_student(self, student: Student):
        if student in self.group_students:
            self.group_students.remove(student)
            Group.stp -= 1

    def find_student_by_surname(self, value: str):
        res = [stud for stud in self.group_students if stud.lastname == value]
        return res or None

    def find_by_char(self, value: str):
        res = [stud for stud in self.group_students if stud.lastname.startswith(value)
               or stud.firstname.startswith(value)]
        return res or None

    def __str__(self, *args, **kwargs):
        res = f'Course: {self.course}\n'
        res += f'Students group:\n\t{"".join(map(str, self.group_students))}\n'
        return res