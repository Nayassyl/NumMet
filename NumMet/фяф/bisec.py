def f(x):
    return x ** 3 + x - 3
def bisection(x0,x1,e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    print('f(%0.8f) = %0.8f, f(%0.8f) = %0.8f' % (x0, f(x0), x1, f(x1))) 
    print()
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x%d = %0.8f and f(x%d) = %0.8f' % (step, step + 1, x2, step + 1,  f(x2)))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        print('f(%0.8f) = %0.8f, f(%0.8f) = %0.8f. Error = %0.8f' % (x0, f(x0), x1, f(x1), abs(f(x2))))
        print()
        step = step + 1
        condition = abs(f(x2)) > e
    print('\nRequired Root is : %0.8f' % x2)

x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(x0,x1,e)