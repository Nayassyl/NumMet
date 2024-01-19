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

list_of_equations = {
    1: x**3 + 2 * x + 2, 2: x**3 - 2 * x + 2, 3: x**3 + 3 * x - 1, 4: x**3 + x - 3, 5: x**3 + 2*x + 4, 6: x * (x+1)**2 - 1,
    7: (x+1)**2 - x, 8: x**3 + 4 * x - 4, 9: x**3 + 6 * x - 1, 10: x**3 + 12 * x - 12, 11: x**3 + 0.4 * x - 1.2,
    12: x**3 + 0.5 * x - 1, 13: x**3 + 2 * x - 4, 14: x**3 + 0.4 * x + 2, 15: x**3 + 9 * x - 11, 16: x**3 + 6 * x + 3,
    17: x**3 + 5 * x - 1, 18: x**3 + 9 * x - 3, 19: x**3 + 10 * x - 5, 20: x**3 + 13 * x - 13, 21: x**3 + 7 * x - 7,
    22: x**3 + 4 * x - 2, 23: x**3 + 5 * x - 4, 24: x**3 + 8 * x - 6, 25: x**3 + 2.5 * x - 4, 26: x**3 + 2.5 * x - 5,
    27: x**3 + 5.5 * x - 2, 28: x**3 + 7 * x - 3, 29: x**3 + 8 * x - 5, 30: x**3 + 15 * x - 10, 31: sympy.log(x) - 1/x,
    32: sympy.cos(x) + 2 * x - 1.5, 33: sympy.log(x) - sympy.sin(x), 34: sympy.log(x) - sympy.cos(x),
    35: sympy.cos(x) - x, 36: sympy.sin(x) + x - 1, 37: sympy.log(x) - x/2 - 1/2,
    38: x**3 - 5 * x**2 + 2 * x + 8, 39: sympy.sin(x) - (1-x**2)**(1/2), 40: x**3 - 2 * x**2 - 5 * x + 6,
}

number_of_equation = int(input())
try:
    if 1 <= number_of_equation <= 40:
        equation = list_of_equations[number_of_equation]
    else:
        raise Exception()
except:
    print("Please enter the number of equation [1, 40]")
    exit()
else:
    if number_of_equation not in [39, 37, 34, 33, 31]:
        domain = np.linspace(-1e2, 1e2, 400)
    else:
        domain = np.linspace(0.01, 10000, 400)
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
             label=list_of_equations[number_of_equation], color="green")
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
