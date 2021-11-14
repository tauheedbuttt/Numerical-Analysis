from math import *


class Polynomial:

    def __init__(self, coef, const):
        self.coef = coef
        self.const = const

    def __str__(self):
        result = ""
        for item in self.coef:
            term = f"{self.coef[item]}x^{item}"
            result += f"({term}) + "
        result += f" ({self.const})"
        return result

    def evaluate(self, value):
        ans = self.const
        for var in self.coef:
            ans += self.coef[var] * (value ** var)
        return ans

    def derivative(self):
        # keeps derivative form of the equation
        der = Polynomial({}, 0)

        for var in self.coef:
            der.coef[var-1] = self.coef[var] * var

        #return the derivative
        return der

    def formula(self, P0):
        f_P0 = self.evaluate(P0)
        f_der_P0 = (self.derivative()).evaluate(P0)
        result = P0 - (f_P0/f_der_P0)
        return result
