import matplotlib.pyplot as plt
import numpy as np
import sympy

def newton_ruphson_method(f, derivative_of_f, initial_point, error=1e-8):
    root = initial_point
    while abs(f(root)) >= error:
        if (derivative_of_f(root) == 0):
            return root
        root = root - f(root) / derivative_of_f(root)
    return root

x = sympy.symbols("x")
equation = x**3 + 3 * x - 1
domain = np.linspace(-1e2, 1e2, 400)
equation = sympy.lambdify(x, equation, modules=['numpy'])
derivative = sympy.diff(equation(x), x)
derivative = sympy.lambdify(x, derivative, modules=['numpy'])
range_values = equation(domain)
plt.figure(figsize=(8, 6))
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.title("Numerical Methods LAB-1")
plt.grid(True)
plt.plot(domain, range_values,
    label=x**3 + 3 * x - 1, color="green")
plt.plot(domain, domain, label="y = x", color="blue", linestyle="--")

root1 = newton_ruphson_method(equation, derivative, 1.0)
root2 = newton_ruphson_method(equation, derivative, -1.0)
plt.scatter([root1, root2], [equation(root1),
    equation(root2)], color="red", marker="o")
plt.annotate(f'Root 1: ({root1:.8f}, {equation(root1):.8f})', xy=(root1, equation(root1)), xytext=(
    root1-10, equation(root1)-10), arrowprops=dict(arrowstyle='->'), fontsize=10, color="red")
plt.annotate(f'Root 2: ({root2:.8f}, {equation(root2):.8f})', xy=(root2, equation(root2)), xytext=(
    root2+1, equation(root2)+1), arrowprops=dict(arrowstyle='->'), fontsize=10, color="red")
print(f'Root 1: ({root1:.8f}, {equation(root1):.8f})')
print(f'Root 2: ({root2:.8f}, {equation(root2):.8f})')
plt.legend()
plt.show()