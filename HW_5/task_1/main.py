# 1) Дополните класс Группа (задание Лекции 2) возможностью поддержки
# итерационного протокола. + добавил протокол последовательности.

from student_subclass import Student
from group import Group

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

# group_1.add_student(student_11)
# group_1.add_student(student_12)
# group_1 = student_12 + group_1
for surname in group_1.find_student_by_surname('Ivanov'):
    print('Was found: ', surname)

for char in group_1.find_by_char('P'):
    print('List of names, starts with "P"', char)

print(group_1)
print('*' * 45)

# по итерации работает
for stud_iter in group_1:
    print(stud_iter)
print('*' * 45)

# по индексу работает
stud_index = group_1[2]
print(stud_index)
print('*' * 45)

# по срезу работает
stud_slise = group_1[5:8]
for stud in stud_slise:
    print(stud)


