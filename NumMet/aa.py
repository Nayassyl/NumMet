def f(x):
    return x**3 + 3 * x - 1
def g(x):
    return (1 - x**3)/3
def fixed_point(initial_point, error=1e-8):
    root = initial_point
    while abs(f(root)) >= error:
        root = g(root)
    return root

print(fixed_point(0))
print(fixed_point(0.5))


