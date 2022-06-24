class Buyer:
    """
    Created class buyer
    """

    def __init__(self, surname, firstname, phon_number, *args, **kwargs):
        self.surname = surname
        self.firstname = firstname
        self.phon_number = phon_number

    def __str__(self):
        return f'{self.surname} - {self.firstname} - {self.phon_number}'