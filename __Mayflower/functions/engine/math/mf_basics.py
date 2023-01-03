import math

class Basic_functions:

    def __init__(self):
        # common symbols
        self.e = math.e
        self.inf = math.inf
        self.pi = math.pi
        self.tau = math.tau

    def zero_proof_division(self, x, y):
        try:
            return x/y
        except ZeroDivisionError:
            return 0
