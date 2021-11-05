from math import *


class trig:
    def __init__(self, trigno, pow=1):
        self.trigno = trigno
        self.pow = pow

    def __str__(self):
        return f"{self.trigno}(x^{self.pow})"

    def __repr__(self):
        return f"{self.trigno}(x^{self.pow})"

    def evaluate(self, x):
        return globals()[self.trigno](x ** self.pow)
