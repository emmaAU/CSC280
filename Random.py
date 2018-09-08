#import random

#print(random.random)

import math
print(math)
a = int(input('enter coefficient for x**2 '))
b = int(input('enter b: '))
c = int(input('what is c?: '))

disc = b**2 - 4*a*c
if disc > 0:
    root1 = -b + math.sqrt(disc) / 2*2
    print(root1)
    root2 = -b - math.sqrt(disc) / 2*2
    print(root2)
elif disc == 0:
    root1 = root2 = -b / 2*2
else:
    print('no roots')

product = 1
n = int(input('please enter a value you want to compute its factorial'))

for i in range(2, n+1):
    product = product * i
print('the factorial of', n, 'is, product')







