class GroupLimit(Exception):

    def __init__(self, desc):
        super().__init__()
        self.desc = desc

    def __str__(self):
        return f"Group is full \n - - - {self.desc}"