a = 3
b = 24
c = 2

#solving quadratic equation without any addition libraries

D = b ** 2 - 4 * a * c
if D < 0:
    print('This equation does not have any roots')
elif D== 0:
    x = -b / (2 * a)
    print(f'x = {x}')
else:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print(f'x1 = {x1}, x2 = {x2}')

#Solving that equation with nympy
import numpy as np
coeffitients = [a, b, c]
roots = np.roots(coeffitients)
print('solving with numpy is', roots)