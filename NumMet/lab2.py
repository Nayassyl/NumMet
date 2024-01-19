from sympy import *
x, y = symbols('x y')
class integrating_function():
    def __init__(self, func, n, initial_point, final_point, constant=1):
        self.function = func
        self.N = n
        self.initial_point = initial_point
        self.final_point = final_point
        self.constant = constant

    def midpoint_method(self):
        midpoint_sum = 0.0
        delta_x = (self.final_point-self.initial_point)/self.N
        for i in range(self.N):
            Mi = (self.initial_point + delta_x/2) + i * delta_x
            midpoint_sum += self.function.subs(x, Mi)
        midpoint_sum *= self.constant
        midpoint_sum = midpoint_sum.evalf()
        print(f"Midpoint approximation = {delta_x * midpoint_sum}\n")
        return delta_x * midpoint_sum

    
    def composite_simpsons_method(self):
        h = (self.final_point - self.initial_point)/self.N
        simpsons_sum = self.function.subs(
            x, self.initial_point) + self.function.subs(x, self.final_point)
        for i in range(1, self.N):
            if i % 2 != 0:
                simpsons_sum += 4 * self.function.subs(x, self.initial_point + i * h)
            else:
                simpsons_sum += 2 * self.function.subs(x, self.initial_point + i * h)
        simpsons_sum *= 1/3 * h
        simpsons_sum *= self.constant
        simpsons_sum = simpsons_sum.evalf()
        print(f"Composite Simpson's  approximation = {simpsons_sum}\n")
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
        simpsons = self.composite_simpsons_method()
        riemanns = self.default_integration()
        print(
            f"Error in midpoint approximation  = {abs(riemanns - midpoint)}\n\nError in simpsons approximation = {abs(riemanns - simpsons)}")
f = integrating_function(2 * x**2 - (3 / 2)*sqrt(x), 6, 1, 4)
f.analysis()
