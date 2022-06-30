class EmptyFile(Exception):

    def __init__(self):
        super().__init__()

    def __str__(self):
        pass