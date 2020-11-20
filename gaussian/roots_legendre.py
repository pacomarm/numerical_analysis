degree = 3    #DEGREE OF LEGENDRE POLYNOMIAL

tol= 0.0001
imax = 100

def f(x):
    return x**3 - 3/5*x

def bisection(left, right):
    a = left
    b = right
    if (f(a) * f(b) > 0 ):
        return print('No hay raiz en el intervalo')
    i = 1
    while i < imax:
        p = a + ((b-a)/2)
        if (abs(f(p) - 0) < tol) or ((b-a)/2) < tol:
            root = p
            return root
        if f(a) * f(p) < 0:
            b = p
        if f(a) * f(p) > 0:
            a = p
        i = i + 1

roots = []

roots.append(bisection(-1,0))
roots.append(bisection(-.5,.5))
roots.append(bisection(.5,1.5))

print(roots)
