import enum as Enum


class period_in_year(Enum):

    Days = 1/365  # : Days = 0
    Weeks = 7/365  # : Weeks = 1
    Months = 1/12  # : Months = 2
    Years = 1  # : Years = 3


class period_holder:

    '''
    class provides a period (length, unit) and implements basic calculation
    '''

    def __init__(self, length: float, unit: str, basic_unit: period_in_year):
        self.length = length
        self.unit = unit
        self.basic_unit = basic_unit

    def convert_to_year(self):
        return self.length * self.basic_unit[self.unit].value, "Years"
