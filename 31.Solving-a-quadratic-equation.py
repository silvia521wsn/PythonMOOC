from math import sqrt
a = int(input('Value of a: '))
b = int(input('Value of b: '))
c = int(input('Value of c: '))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + sqrt(delta))/(a*2)
    x2 = (-b - sqrt(delta))/(a*2)
    print(f'The roots are {x1} and {x2}')
elif delta == 0:
    x = -b / (2 * a)
    print(f'The root is {x}')
else:
    print('There are no real roots')