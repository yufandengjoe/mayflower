import numbers
from enum import Enum
from datetime import datetime


class data_type(Enum):

    Bool: bool
    Integer: int
    Real: float
    Decimal: float
    Size: int
    Time: datetime
    String: str
    Complex: str

    Rate: float
    Spread: float
    Volatility: float
    Discount_factor: float
    Probability: float


def is_number(number):
    return (number is not None) and \
           (isinstance(
            number, int) or isinstance(
            number, float) or isinstance(
                number, numbers.Integral))
