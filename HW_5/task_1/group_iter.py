
class GroupIter:

    def __init__(self, group_students):
        self.group_students = group_students
        self.index = 0

    def __next__(self):
        if self.index < len(self.group_students):
            self.index = self.index + 1
            return self.group_students[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self
