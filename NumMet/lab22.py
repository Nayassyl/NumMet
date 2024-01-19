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
        temp_x = self.x0
        temp_y = self.y0
        points = [(self.x0, self.y0)]
        while temp_x < self.final_point:
            temp_y = temp_y + self.height * \
                self.function.subs({x: temp_x, y: temp_y})
            temp_x += self.height
            points.append((temp_x, temp_y,))
            
        return points

    def improved_eulers_method(self):
        temp_x = self.x0
        temp_y = self.y0
        points = [(self.x0, self.y0)]
        while temp_x < self.final_point:
            temp1 = self.function.subs({x:temp_x, y: temp_y})
            temp2 = self.function.subs({x:(temp_x + self.height) , y: (temp_y) + self.height * temp1})
            temp_x += self.height
            temp_y = temp_y + (self.height / 2) * (temp1 + temp2)
            points.append((temp_x, temp_y,))
        return points

    def runge_kutta_method(self):
        temp_x = self.x0
        temp_y = self.y0
        points = [(self.x0, self.y0,)]
        while temp_x < self.final_point:
            temp_k1 = self.function.subs({x: temp_x, y: temp_y})
            temp_k2 = self.function.subs(
                {x: temp_x + self.height/2, y: temp_y + self.height/2 * temp_k1})
            temp_k3 = self.function.subs(
                {x: temp_x + self.height/2, y: temp_y + self.height/2 * temp_k2})
            temp_k4 = self.function.subs(
                {x: temp_x + self.height, y: temp_y + self.height * temp_k3})
            temp_y = temp_y + (self.height/6) *(temp_k1 + 2 * temp_k2 + 2 * temp_k3 + temp_k4)
            temp_x += self.height
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
        print("\ny points of exact solution:", y_exacts)
        for i in range(len(x_values)):
            print(
                f"\nAt point x = {x_values[i]}:\nEuler's method y = {y_eulers[i]}\nError:{abs(y_exacts[i] - y_eulers[i])}")
            print(
                f"Heun's method y = {y_improved_eulers[i]}\nError:{abs(y_exacts[i] - y_improved_eulers[i])}")
            print(
                f"Runge-Kuttas method y = {y_runge_kuttas[i]}\nError:{abs(y_exacts[i] - y_runge_kuttas[i])}")
            print()
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

f = equation((x ** 3) * (y ** 4) - y / x , 1, 1 / 2, 1, 2, 0.2)
print("Euler's method's values:" , f.eulers_method())
print("\nHeun's method's values:", f.improved_eulers_method())
print("\nEquation of exact solution:", f.exact_solution())

f.solutions_graph()