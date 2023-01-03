import enum as Enum


class Option_type(Enum):

    Call = 1
    Put = -1


class Exerise_type(Enum):

    European = 'european'
    American = 'american'


class Option():

    def __init__(self,
                 option_type: Option_type,  # "call" or "put"
                 spot_rate,
                 strike,
                 maturity,
                 vol=None,
                 riskless_rate=None,
                 yield_=None,  # input can be function to calculate yield or constant
                 exerise_type: Exerise_type = None  # “European”/“American”
                 ):

        self.option_type = option_type
        self.spot_rate = spot_rate
        self.strike = strike
        self.vol = vol
        self.maturity = maturity
        self.riskless_rate = riskless_rate or 0
        self.yield_ = yield_ or 0
        self.exerise_type = exerise_type

        self.model_cache = {}
        self.model_cache_param_hashes = {}
        return None

    def copy(self):
        return Option(option_type=self.option_type,
                      spot_rate=self.spot_rate,
                      strike=self.strike,
                      maturity=self.maturity,
                      vol=self.vol,
                      riskless_rate=self.riskless_rate,
                      yield_=self.yield_,
                      exerise_type=self.exerise_type)

    def param_hash(self):
        return hash((self.option_type,
                     self.spot_rate,
                     self.strike,
                     self.maturity,
                     self.vol,
                     self.riskless_rate,
                     self.yield_,
                     self.exerise_type))
