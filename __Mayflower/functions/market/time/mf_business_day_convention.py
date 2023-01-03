from enum import Enum


class BusinessDayConvention(Enum):

    Following = "Following"
    ModifiedFollowing = "ModifiedFollowing"
    Preceding = "Preceding"
    ModifiedPreceding = "ModifiedPreceding"
    Unadjusted = "Unadjusted"
    HalfMonthModifiedFollowing = "HalfMonthModifiedFollowing"
    Nearest = "Nearest"