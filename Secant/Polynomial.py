from Trig import *
from math import *


class Polynomial:

    def __init__(self, coef, const):
        self.coef = coef
        self.const = const

    def __str__(self):
        result = ""
        for item in self.coef:
            term = ""
            if type(item).__name__ == "trig":
                term = f"{self.coef[item]}{item}"
            else:
                term = f"{self.coef[item]}x^{item}"
            result += f"({term}) + "
        result += f" ({self.const})"
        return result

    def evaluate(self, value):
        ans = self.const
        for var in self.coef:
            if type(var).__name__ == "trig":
                ans += self.coef[var] * var.evaluate(value)
            else:
                ans += self.coef[var] * (value ** var)
        return ans

    def formula(self, P0, P1):
        f_P0 = self.evaluate(P0)
        f_P1 = self.evaluate(P1)
        num = (f_P1 * P0) - (f_P0 * P1)
        den = f_P1 - f_P0
        return num / den
