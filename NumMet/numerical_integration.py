from sympy import *
x, y = symbols('x y')
# init_printing(use_unicode=True)


class integrating_function():
    def __init__(self, func, n, initial_point, final_point, constant=1):
        self.function = func
        self.N = n
        self.initial_point = initial_point
        self.final_point = final_point
        self.constant = constant

    def midpoint_method(self):
        if self.initial_point == 0:
            h = self.final_point
            midpoint_function = h * self.function.subs(x, h/2) + (h**3/24) * diff(
                self.function, x, 2).subs(x, h/2) + (h**5/1920) * diff(self.function, x, 4).subs(x, h/2)
            midpoint_function *= self.constant
            midpoint_function = midpoint_function.evalf()
            print(
                f"If borders are in form [0,h] midpoint approximation = {midpoint_function}\n")
            return midpoint_function
        else:
            midpoint_sum = 0.0
            delta_x = (self.final_point-self.initial_point)/self.N
            for i in range(self.N):
                Mi = (self.initial_point + delta_x/2) + i * delta_x
                midpoint_sum += self.function.subs(x, Mi)
            midpoint_sum *= self.constant
            midpoint_sum = midpoint_sum.evalf()
            print(f"Midpoint approximation = {delta_x * midpoint_sum}\n")
            return delta_x * midpoint_sum

    def trapezoidal_method(self):
        if self.initial_point == 0:
            h = self.final_point
            trapezoidal_function = h/2 * (self.function.subs(x, 0) + self.function.subs(x, h)) - h**3 / 12 * diff(
                self.function, x, 2).subs(x, h/2) - h ** 5/480 * diff(self.function, x, 4).subs(x, h/2)
            trapezoidal_function *= self.constant
            trapezoidal_function = trapezoidal_function.evalf()
            print(
                f"If borders are in form [0,h] trapezoidal approximation = {trapezoidal_function}\n")
            return trapezoidal_function
        else:
            trapezoidal_sum = left_sum = right_sum = 0
            delta_x = (self.final_point - self.initial_point)/self.N
            temp_x = self.initial_point
            subintervals = [temp_x]
            for i in range(self.N):
                temp_x += delta_x
                subintervals.append(temp_x)
            for i in range(self.N):
                trapezoidal_sum += (self.function.subs(
                    x, subintervals[i]) + self.function.subs(x, subintervals[i+1]))/2
                left_sum += self.function.subs(x, subintervals[i])
                right_sum += self.function.subs(x, subintervals[i+1])
            left_sum *= self.constant
            right_sum *= self.constant
            trapezoidal_sum *= self.constant
            left_sum = left_sum.evalf()
            right_sum = right_sum.evalf()
            trapezoidal_sum = trapezoidal_sum.evalf()
            print(
                f"Left sum = {left_sum * delta_x}\n\nRight sum = {right_sum * delta_x}\n")
            print(
                f"Directly trapezoidal approximation = {trapezoidal_sum * delta_x}\n\nWith left and right sums = {(left_sum + right_sum)/2 * delta_x}\n")
            return trapezoidal_sum

    def simpsons_method(self):
        if self.initial_point == 0:
            h = self.final_point/2
            simpsons_function = h/3 * \
                (self.function.subs(x, 0) + 4 *
                 self.function.subs(x, h) + self.function.subs(x, 2 * h))
            simpsons_function *= self.constant
            simpsons_function = simpsons_function.evalf()
            print(f"If borders are in form [0,2h] simpsons approximation = {simpsons_function}\n")
            return simpsons_function
        else:
            h = (self.final_point - self.initial_point)/self.N
            simpsons_sum = self.function.subs(
                x, self.initial_point) + self.function.subs(x, self.final_point)
            for i in range(1, self.N):
                if i % 3 == 0:
                    simpsons_sum += 2 * \
                        self.function.subs(x, self.initial_point + i * h)
                else:
                    simpsons_sum += 3 * \
                        self.function.subs(x, self.initial_point + i * h)
            simpsons_sum *= 3/8 * h
            simpsons_sum *= self.constant
            simpsons_sum = simpsons_sum.evalf()
            print(f"Simpson's 3/8 approximation = {simpsons_sum}\n")
            return simpsons_sum

    def default_integration(self):
        riemann_sum = integrate(
            self.function, (x, self.initial_point, self.final_point))
        riemann_sum *= self.constant
        riemann_sum = riemann_sum.evalf()
        print(f"Directly integration = {riemann_sum}\n")
        return riemann_sum

    def analysis(self):
        midpoint = self.midpoint_method()
        trapezoidal = self.trapezoidal_method()
        simpsons = self.simpsons_method()
        riemanns = self.default_integration()
        print(
            f"Error in midpoint approximation  = {abs(riemanns - midpoint)}\n\nError in trapezoidal approximation = {abs(riemanns-trapezoidal)}\n\nError in simpsons approximation = {abs(riemanns - simpsons)}")


list_of_functions = {
    1: integrating_function(2 * x**2 - sqrt(x + 2), 6, -2, 4),
    2: integrating_function(5 * x ** 2 + x + 1, 6, -3, 0),
    3: integrating_function(3 * x**2 - sqrt(x), 6, 0, 3),
    4: integrating_function(x**3 - sqrt(x), 6, 1, 4),
    5: integrating_function(7 + x - 2 * x**2, 6, 1, 4),
    6: integrating_function(7 * x ** 2 - 3 * sqrt(x), 6, 0, 3),
    7: integrating_function(2 * x ** 2 - 2 - sqrt(x), 6, 2, 5),
    8: integrating_function(5 * x**2 + sqrt(x), 6, 0, 3),
    9: integrating_function(x**3 + 1, 8, -2, 2),
    10: integrating_function(2 * x**2 + 1 - sqrt(x), 8, 0, 4),

    11: integrating_function(x**2 + sqrt(x + 2) - 1, 8, -2, 2),
    12: integrating_function(x**2 + 2 + sqrt(x), 8, 0, 2),
    13: integrating_function(3 * x**2 - x - 1, 8, 1, 3),
    14: integrating_function(x**3 + 2, 8, -1, 3),
    15: integrating_function(2 * x**2 + 1 - sqrt(x+4), 8, -2, 2),
    16: integrating_function(2 * x ** 2 - 1.5 * sqrt(x), 6, 1, 4),
    17: integrating_function(7 * sqrt(x) + 2 * x**2, 6, 1, 4),
    18: integrating_function(7 * x**2 + 3 * sqrt(x), 6, 0, 3),
    19: integrating_function(2 * x ** 2 + sqrt(x) - 2, 6, 2, 5),
    20: integrating_function(5 * x**2 + sqrt(x) - 1, 6, 0, 3),

    21: integrating_function(x**2 + 4 + sqrt(x), 6, 3, 6),
    22: integrating_function(x**3 + 3, 8, 3, 6),
    23: integrating_function(2 * x ** 2 + sqrt(x) - 1, 6, 0, 3),
    24: integrating_function(3 * x**2 + 2 * sqrt(x + 2), 8, -2, 2),
    25: integrating_function(x**2 + 2 * sqrt(x+2), 8, -2, 2),
    26: integrating_function(x**2 + 2 * x - 1.5, 6, -3, 1),
    27: integrating_function(3 * x**2 + sqrt(x + 3) + 1, 6, -3, 0),
    28: integrating_function(3 * x**2 + sqrt(x) + 5, 6, 0, 3),
    29: integrating_function(exp(-(x**2/2)), 10, 0, 1, 1/sqrt(2 * pi)),
    30: integrating_function(1/(1 + sqrt(x)), 10, 0, 1)}


