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
    def a(self):
        elem = int(((self.final_point - self.initial_point) / self.height) + 1)
        runge_kuttas = self.runge_kutta_method()
        x_values = [point[0] for point in runge_kuttas]
        # x_values = [float(self.initial_point + i * self.height) for i in range(elem + 1)]
        return x_values

f = equation(1 - x + y, 1.1, 0, 1.1, 1.6, 0.1)
print(f.a())