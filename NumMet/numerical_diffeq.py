from sympy import *
import matplotlib.pyplot as plt
x, y = symbols('x y')


class equation:
    def __init__(self, function, x0, y0, initial_point, final_point, height):
        self.function = function
        self.y0 = y0
        self.x0 = x0
        self.initial_point = initial_point
        self.final_point = final_point
        self.height = height

    def eulers_method(self):
        temp_y = self.y0 + self.height * \
            self.function.subs({x: self.x0, y: self.y0})
        temp_x = self.x0
        points = [(self.x0, self.y0)]
        while temp_x < self.final_point:
            temp_x += self.height
            temp_y = temp_y + self.height * \
                self.function.subs({x: temp_x, y: temp_y})
            points.append((temp_x, temp_y,))
        return points

    def improved_eulers_method(self):
        temp_y = self.y0 + (self.height/2) * (self.function.subs({x: self.x0, y: self.y0}) + self.function.subs(
            {x: self.x0 + self.height, y: self.y0 + self.height * self.function.subs({x: self.x0, y: self.y0})}))
        temp_x = self.x0
        points = [(self.x0, self.y0)]
        while temp_x < self.final_point:
            temp_x += self.height
            temp_y = temp_y + self.height/2 * (self.function.subs({x: temp_x, y: temp_y}) + self.function.subs(
                {x: temp_x + self.height, y: temp_y + self.height * self.function.subs({x: temp_x, y: temp_y})}))
            points.append((temp_x, temp_y,))
        return points

    def runge_kutta_method(self):
        temp_k1 = self.function.subs({x: self.x0, y: self.y0})
        temp_k2 = self.function.subs(
            {x: self.x0 + self.height/2, y: self.y0 + self.height/2 * temp_k1})
        temp_k3 = self.function.subs(
            {x: self.x0 + self.height/2, y: self.y0 + self.height/2 * temp_k2})
        temp_k4 = self.function.subs(
            {x: self.x0 + self.height, y: self.y0 + self.height * temp_k3})
        temp_y = self.y0 + self.height/6 * \
            (temp_k1 + 2 * temp_k2 + 2 * temp_k3 + temp_k4)
        temp_x = self.x0
        points = [(self.x0, self.y0,)]
        while temp_x < self.final_point:
            temp_x += self.height
            temp_k1 = self.function.subs({x: temp_x, y: temp_y})
            temp_k2 = self.function.subs(
                {x: temp_x + self.height/2, y: temp_y + self.height/2 * temp_k1})
            temp_k3 = self.function.subs(
                {x: temp_x + self.height/2, y: temp_y + self.height/2 * temp_k2})
            temp_k4 = self.function.subs(
                {x: temp_x + self.height, y: temp_y + temp_k3})
            temp_y = temp_y + self.height/6 * \
                (temp_k1 + 2 * temp_k2 + 2 * temp_k3 + temp_k4)
            points.append((temp_x, temp_y,))
        return points

    def exact_solution(self):
        u = symbols('u')
        v = Function('v')(u)
        diff_eq = Eq(v.diff(u), self.function.subs({x: u, y: v}))
        solution = dsolve(diff_eq, ics={v.subs(u, self.x0): self.y0})
        solution = solution.rhs.subs({u: x})
        return solution

    def solutions_graph(self):
        eulers = self.eulers_method()
        improved_eulers = self.improved_eulers_method()
        runge_kuttas = self.runge_kutta_method()
        solution = self.exact_solution()
        x_values = [point[0] for point in runge_kuttas]
        y_eulers = [point[1] for point in eulers]
        y_improved_eulers = [point[1] for point in improved_eulers]
        y_runge_kuttas = [point[1] for point in runge_kuttas]
        y_exacts = [solution.subs({x: point}).evalf() for point in x_values]
        print(
            f"At point x = {x_values[-1]}:\n\nEuler's method y = {y_eulers[-1]}\nError:{abs(y_exacts[-1] - y_eulers[-1])}\n")
        print(
            f"Heun's method y = {y_improved_eulers[-1]}\nError:{abs(y_exacts[-1] - y_improved_eulers[-1])}\n")
        print(
            f"Runge-Kuttas method y = {y_runge_kuttas[-1]}\nError:{abs(y_exacts[-1] - y_runge_kuttas[-1])}")
        plt.plot(x_values, y_eulers, label="Euler's method", color="red")
        plt.plot(x_values, y_improved_eulers,
                 label="Heun's method", color="green")
        plt.plot(x_values, y_runge_kuttas,
                 label="Runge-Kuttas method", color="blue")
        plt.plot(x_values, y_exacts, label="Exact solution", color="black")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()


list_of_equations = {
    1: equation(3 + 2 * x - y, 0, 2, 0, 1, 0.2),
    2: equation(y - 3 * x, 1, 0, 1, 2.2, 0.3),
    3: equation(1 - x + y, 1.1, 0, 1.1, 1.6, 0.1),
    4: equation(y - 7 * x, 3, 3, 3, 5, 0.5),
    5: equation(5 - y + x, 1, 1, 1, 5, 0.1),
    6: equation(y - 2 * x + 3, 0, 4, 0, 1, 0.2),
    7: equation(4 - x + 2 * y, 0, 1, 0, 1.2, 0.3),
    8: equation(-8 + 2 * x - y, 1, 3, 1, 3, 0.4),

    9: equation(2 * y - 3 * x, 4, 0, 4, 6, 0.5),
    10: equation(x - 2 * y, -1, 1, -1, 2, 0.6),
    11: equation(7 - x * y, -2, 0, -2, 0, 0.5),
    12: equation(2 * x + y, 2, 2, 2, 3.5, 0.5),
    13: equation(5 + x - y, 2, 1, 2, 4, 0.5),
    14: equation(y + 5 * x - 1, 0, 2, 0, 3.2, 0.8),
    15: equation(y - 5 * x + 1, 0, 2, 0, 3.2, 0.8),
    16: equation(1 - x + y, 0, 1, 0, 2.5, 0.5),

    17: equation(y - 5 * x, -1, 1, -1, 1, 0.4),
    18: equation(x + 2 * y, 0, -1, 0, 2, 0.4),
    19: equation(x + y + 2, 1, 1, 1, 3, 0.5),
    20: equation(3 * x + 4 * y, 2, 1, 2, 5, 0.5),
    21: equation(3 + 2 * x + y, 0, 2, 0, 1, 0.2),
    22: equation(2 * y - x, 1, 0, 1, 2.2, 0.2),
    23: equation(-x + y, 1.1, 0, 1.1, 1.6, 0.1),
    24: equation(y - 7 * x + 2, 3, 3, 3, 5,0.5),

    25: equation(5 - y + x, 1, 1, 1, 5, 0.1),
    26: equation(y - 2 * x + 3, 0, 4, 0, 1, 0.2),
    27: equation(4 - x + 2 * y, 0, 1, 0, 1.2, 0.3),
    28: equation(-8 + 2 * x - y, 1, 3, 1, 3, 0.4),
    29: equation(2 * y - 3 * x, 4, 0, 4, 6, 0.5),
    30: equation(x * x - 2 * y, -1, 1, -1, 2, 0.5),
    31: equation(5 - x - 2 * y, 1, 2, 2, 4, 0.5),
    32: equation(y + 3 * x - 2, 1, 2, 1, 2, 0.2),
}
list_of_equations[3].solutions_graph()
