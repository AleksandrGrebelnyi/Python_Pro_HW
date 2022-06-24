class GroupLimit(Exception):

    def __init__(self, limit, desc):
        self.desc = desc

    def __str__(self):
        return f"Group is full \n - - - {self.desc}"