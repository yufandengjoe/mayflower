from enum import Enum


class Month(Enum):

    # Map the correct value to months
    January   = 1
    February  = 2
    March     = 3
    April     = 4
    May       = 5
    June      = 6
    July      = 7
    August    = 8
    September = 9
    October   = 10
    November  = 11
    December  = 12

    # Assigning the same value means alias 
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12


class Weekday(Enum):

    # Map the correct value to weekdays
    Sunday    = 1
    Monday    = 2
    Tuesday   = 3
    Wednesday = 4
    Thursday  = 5
    Friday    = 6
    Saturday  = 7

    # Alias to weekdays
    Sun = 1
    Mon = 2
    Tue = 3
    Wed = 4
    Thu = 5
    Fri = 6
    Sat = 7


class Oracle_month(Enum):

    # Month object for oracle SQL query
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12