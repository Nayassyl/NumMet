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
equation = x**3 + 9 * x - 11
domain = np.linspace(-1e2, 1e2, 500)
equation = sympy.lambdify(x, equation, modules=['numpy'])
range_values = equation(domain)
plt.figure(figsize=(8, 6))
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.title("Numerical Methods LAB-1")
plt.grid(True)
plt.plot(domain, range_values,
    label=x**3 + 9 * x - 11, color="green")
plt.plot(domain, domain, label="y = x", color="blue", linestyle="--")
root1 = fixed_point_method(0)
root2 = fixed_point_method(1)
plt.scatter([root1, root2], [equation(root1),
    equation(root2)], color="red", marker="o")
print(f'Root 1: ({root1:.10f}, {equation(root1):.10f})')
print(f'Root 2: ({root2:.10f}, {equation(root2):.10f})')
plt.legend()
plt.show()