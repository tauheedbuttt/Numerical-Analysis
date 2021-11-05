from Polynomial import *
from Trig import *
from Secant import *
from math import *


fx = Polynomial(
    {
        3: -1,
        trig("cos"): -1
    }, 0
)
print(f"f(x) = {fx}")

p0 = -1
p1 = 0
n = 10

pn_s = secant_iterations(fx, p0, p1, n)
pn_r = regular_falsi_iterations(fx, p0, p1, n)

print(f"\nP\t\tSecant\t\t Regula-False")
for i in range(n):
	print(f"{i} \t {'%.10f' % pn_s[i]} \t {'%.10f' % pn_r[i]}")
