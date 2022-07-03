from student_subclass import Student
from settings import LIMIT_OF_STUDENTS
from group_iter import GroupIter


class Group:

    def __init__(self, course: str):
        self.course = course
        self.group_students = []

    def add_student(self, student: Student):
        if student not in self.group_students and len(self.group_students) < LIMIT_OF_STUDENTS:
            self.group_students.append(student)

    def remove_student(self, student: Student):
        if student in self.group_students:
            self.group_students.remove(student)

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

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index <= len(self.group_students):
                return self.group_students[index]
            else:
                raise IndexError
        if isinstance(index, slice):
            slice_group = []
            start = 0 if index.start is None else index.start
            stop = len(self.group_students) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            if index.start < 0 and index.stop > len(self.group_students):
                raise IndexError
            for i in range(start, stop, step):
                slice_group.append(self.group_students[i])
            return slice_group
        raise TypeError()

    def __len__(self):
        return len(self.group_students)

    def __iter__(self):
        return GroupIter(self.group_students)