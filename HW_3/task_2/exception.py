class GroupLimit(Exception):

    def __init__(self, limit, desc):
        super().__init__()
        self.limit = limit
        self.desc = desc

    def __str__(self):
        return f"AmountError \n{self.limit} - {self.desc}"