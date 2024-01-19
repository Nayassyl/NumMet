import matplotlib.pyplot as plt
import numpy as np
import sympy
def f(x):
    return x**3 + 9 * x - 11
def g(x):
    return (11 - x**3)/9
def fixed_point_method(initial_point, error=1e-8):
    root = initial_point
    while abs(f(root)) >= error:
        root = g(root)
    return root
x = sympy.symbols("x")
equation = x
g_equation = (11 - x**3)/9
domain = np.linspace(-10, 10, 400)
equation = sympy.lambdify(x, equation, modules=['numpy'])
g_equation = sympy.lambdify(x, g_equation, modules = ['numpy'])
range_values = equation(domain)
range_valuesss = g_equation(domain)
plt.figure(figsize=(8, 6))
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.title("Numerical Methods LAB-1")
plt.grid(True)
plt.plot(domain, range_values,
    label=x, color="blue")
plt.plot(domain, range_valuesss, label = (11 - x**3)/9 , color = 'yellow')

plt.legend()
plt.show()