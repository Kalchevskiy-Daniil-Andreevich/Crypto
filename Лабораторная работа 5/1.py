from sympy import symbols, Poly, div

x = symbols('x')

polynomial = Poly(x**5 + x**3 + 1, x)

r = 5

n = 2**r - 1
k = n - polynomial.degree()

print("(n, k)-Code: ({}, {})".format(n, k))
