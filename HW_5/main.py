# 1) Создайте класс, описывающий человека (создайте метод, выводящий
# информацию о человеке).
# 2) На его основе создайте класс Студент (переопределите метод вывода
# информации).
# 3) Создайте класс Группа, который содержит список из 10 объектов класса
# Студент. Реализуйте методы добавления, удаления студента и метод поиска
# студента по фамилии. Определите для Группы метод __str__() для
# возвращения списка студентов в виде строки.


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
# group_1.add_student(student_10)

# group_1.add_student(student_11)
# group_1.add_student(student_12)
# group_1 = student_12 + group_1
for surname in group_1.find_student_by_surname('Ivanov'):
    print('Was found: ', surname)

for char in group_1.find_by_char('P'):
    print('List of names, starts with "P"', char)

print(group_1)
print('*' * 45)

for stud in group_1:
    print(stud)