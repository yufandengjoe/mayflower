import enum as Enum


class DayCounter(Enum):

    Actual360 = 'Actual360'
    Actual365Fixed = "Actual365Fixed"
    Business252 = "Business252"
    OneDayCounter = "OneDayCounter"
    SimpleDayCounter = "SimpleDayCounter"
    Thirty360 = "Thirty360"
    ActualActual = "ActualActual"

