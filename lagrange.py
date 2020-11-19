import numpy as np

x = np.array([2,2.75, 4], float)
y = np.array([.5, 0.3636363636, .25], float)

xp = float(input("Enter x to approximate: "))
yp = 0

for xi, yi in zip(x, y):
    yp += yi * np.prod((xp - x[x != xi])/(xi - x[x != xi]))

print('For x = %.5f, y = %.5f' % (xp,yp))
 