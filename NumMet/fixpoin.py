import math
def f(x):
    return x**3 + 9 * x - 11
def g(x):
    return (11 - x ** 3)/9
def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        err = abs(x0 - x1)
        print('Iteration-%d, x1 = %0.8f and f(x1) = %0.8f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x0)) > e
    if flag == 1:
        print('\nRequired root is: %0.10f' % x1)
    else:
        print('\nNot Convergent.')

x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))
fixedPointIteration(x0, e, N)