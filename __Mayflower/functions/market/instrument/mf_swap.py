import enum as Enum
from functions.market.time import mf_frequency, mf_business_day_convention, mf_day_counter

class Swap_type(Enum):

    Payer = -1
    Receiver = 1

class Swap():

    def __init__(self,
                 swap_type: Swap_type,  # "payer" as -1 or "receiver" as 1
                 fix_rate,

                 fixed_freqency: mf_frequency.Frequency,
                 fixed_convensions: mf_business_day_convention.BusinessDayConvention,
                 fixed_day_counter: mf_day_counter.DayCounter,

                 floating_frequency: mf_frequency.Frequency,
                 floating_convensions: mf_business_day_convention.BusinessDayConvention,
                 floating_day_counter: mf_day_counter.DayCounter
                 ):

        self.swap_type = swap_type
        self.fix_rate = fix_rate

        self.fixed_freqency = fixed_freqency
        self.fixed_convensions = fixed_convensions
        self.fixed_day_counter = fixed_day_counter

        self.floating_frequency = floating_frequency
        self.floating_convensions = floating_convensions
        self.floating_day_counter = floating_day_counter

        self.model_cache = {}
        self.model_cache_param_hashes = {}
        return None

    def copy(self):
        return Swap(
            swap_type = self.swap_type,
            fix_rate = self.fix_rate, 

            fixed_freqency = self.fixed_freqency,
            fixed_convensions = self.fixed_convensions,
            fixed_day_counter = self.fixed_day_counter,

            floating_frequency = self.floating_frequency,
            floating_convensions = self.floating_convensions,
            floating_day_counter = self.floating_day_counter
        )

    def param_hash(self):
        return hash((
            self.swap_type,
            self.fix_rate,

            self.fixed_freqency,
            self.fixed_convensions,
            self.fixed_day_counter,

            self.floating_frequency,
            self.floating_convensions,
            self.floating_day_counter,
        ))

    