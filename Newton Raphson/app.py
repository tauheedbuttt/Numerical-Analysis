from Polynomial import *

def newton_raphson_iterations(fx, p0, n):
    pn = [p0]
    for i in range(1, n+1):
        ans = fx.formula(pn[i-1])
        pn.append(ans)
    return pn

fx = Polynomial(
    {
        3: 1,
        2: -7,
        1: 14,
    }, -6
)
print(f"f(x) = {fx}")

p0 = [0,1]
n = 10

pn = newton_raphson_iterations(fx, p0[0], n)

print(f"\nP\tNewton Raphson")
for i in range(len(pn)):
	print(f"{i} \t {'%.4f' % pn[i]}")
