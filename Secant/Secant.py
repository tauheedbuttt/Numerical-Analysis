from Polynomial import *
from Trig import *
from math import *


def swap(f_p0, f_p1):
    return f_p1, f_p0


def secant_iterations(fx, p0, p1, n):
    pn = [p0, p1]
    for i in range(2, n):
        ans = fx.formula(p0, p1)
        p0, p1 = p1, ans
        pn.append(ans)
    return pn


def regular_falsi_iterations(fx, p0, p1, n):
    pn = [p0, p1]

    for i in range(2, n):
        if (fx.evaluate(p0) > 0) and (fx.evaluate(p1) < 0):
            p0, p1 = p1, p0
        ans = fx.formula(p0, p1)
        p0, p1 = p1, ans
        pn.append(ans)

    return pn


