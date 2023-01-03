import enum as Enum

class Schedule(Enum):

    Backward = "Backward" # Backward from termination date to effective date.
    Forward = "Forward"  # Forward from effective date to termination date.
    Zero = "Zero"     # No intermediate dates between effective date and termination date.
    ThirdWednesday = "ThirdWednesday" # All dates but effective date and termination
                    # date are taken to be on the third wednesday
                    # of their month (with forward calculation.)
    Twentieth = "Twentieth" # All dates but the effective date are taken to be the
                # twentieth of their month (used for CDS schedules in
                # emerging markets.)  The termination date is also modified.
    TwentiethIMM = "TwentiethIMM" # All dates but the effective date are taken to be the
                    # twentieth of an IMM month (used for CDS schedules.)  The
                    # termination date is also modified.
    OldCDS = "OldCDS" # Same as TwentiethIMM with unrestricted date ends and log/short
            # stub coupon period (old CDS convention).
    CDS = "CDS" # Credit derivatives standard rule since 'Big Bang' changes in 2009.
    CDS2015 = "CDS2015" # Credit derivatives standard rule since December 20th, 2015.