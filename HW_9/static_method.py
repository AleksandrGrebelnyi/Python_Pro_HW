# Для класса Box напишите статический метод, который будет подсчитывать
# суммарный объем двух ящиков, которые будут его параметрами

class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Box: x = {self.x}, y = {self.y}, z = {self.z}"

    def volume(self):
        return self.z * self.x * self.y

    @staticmethod
    def volume_two_box(x1, y1, z1, x2, y2, z2):
        return x1 * y1 * z1 + x2 * y2 * z2


box_1 = Box(1, 2, 3)
box_2 = Box(6, 5, 4)
print(box_2.volume())
print(box_1.volume())
box_3 = Box.volume_two_box(1, 2, 3, 4, 5, 6)
print(box_1, box_2, box_3, sep='\n')