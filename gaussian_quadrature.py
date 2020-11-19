import math

n = 3
x = [0.7745966692, 0.0000000000, -0.7745966692]
c = [0.5555555556, 0.8888888889,  0.5555555556]
total = 0
subtotal = 0 

def f( x ):
    return (x**6) - (x**2)*(math.sin(2*x))

for i in range(n):
    subtotal = c[i] * f(x[i])
    print(subtotal)
    total += subtotal

print('The result of the Gaussian Quadrature is: ' + str(total))