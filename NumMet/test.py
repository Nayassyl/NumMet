import numpy as np
import matplotlib.pyplot as plt

def ode_func(x, y):
    return y - 3*x

def euler_method(x0, y0, h, num_steps):
    x_values = [x0]
    y_values = [y0]
    for _ in range(num_steps):
        x0 = x0 + h
        y0 = y0 + h * ode_func(x0, y0)
        x_values.append(x0)
        y_values.append(y0)
    return x_values, y_values

def heun_method(x0, y0, h, num_steps):
    x_values = [x0]
    y_values = [y0]
    for _ in range(num_steps):
        x0 = x0 + h
        k1 = ode_func(x0, y0)
        k2 = ode_func(x0 + h, y0 + h * k1)
        y0 = y0 + 0.5 * h * (k1 + k2)
        x_values.append(x0)
        y_values.append(y0)
    return x_values, y_values

x0 = 0
y0 = 1.0
h = 0.1
num_steps = 100

euler_x, euler_y = euler_method(x0, y0, h, num_steps)

heun_x, heun_y = heun_method(x0, y0, h, num_steps)

plt.plot(euler_x, euler_y, label="Euler's Method")
plt.plot(heun_x, heun_y, label="Heun's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()