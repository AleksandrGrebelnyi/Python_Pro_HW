# 2) Модифицируйте класс Группа (задание прошлой лекции) так, чтобы при
# попытке добавления в группу более 10-ти студентов, было возбужденно
# пользовательское исключение. Таким образом нужно создать еще и
# пользовательское исключение для этой ситуации. И обработать его.
from exception import GroupLimit
from student import Student
from group import Group

if __name__ == '__main__':

    student_1 = Student('Ivan', 'Pupkin', 20)
    student_2 = Student('Valera', 'Reza', 19)
    student_3 = Student('Sasha', 'Zib', 20)
    student_4 = Student('Petr', 'Kira', 20)
    student_5 = Student('Sergey', 'Loza', 18)
    student_6 = Student('Pasha', 'Faster', 20)
    student_7 = Student('Valera', 'Guba', 20)
    student_8 = Student('Aleks', 'Lusha', 20)
    student_9 = Student('Ivan', 'Ivanov', 19)
    student_10 = Student('Oleh', 'Istratov', 19)
    student_11 = Student('Vaska', 'Petrov', 20)
    student_12 = Student('Pedro', 'Robz', 20)

    group_1 = Group('Python')
    try:
        group_1.add_student(student_1)
        group_1.add_student(student_2)
        group_1.add_student(student_3)
        group_1.add_student(student_4)
        group_1.add_student(student_5)
        group_1.add_student(student_6)
        group_1.add_student(student_7)
        group_1.add_student(student_8)
        group_1.add_student(student_9)
        group_1.add_student(student_10)
        group_1.add_student(student_11)
    except GroupLimit as gl:
        print(gl, 'Try later')

    group_2 = Group('Java')
    group_2.add_student(student_11)
    group_2.add_student(student_12)
    group_2.remove_student(student_12)

    print(group_1, group_2, '\n' + 'General amount of students ', Group.stp)




