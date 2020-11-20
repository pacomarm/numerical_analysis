tol= 0.00000001
imax = 100

def f(x):
    # return (x**3) - 3/5*x
    # return 1/8*(35*(x**4) - 30*(x**2)+3)
    return 1/8*(63*(x**5) - 70*(x**3)+15*x)

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

# roots.append(bisection(-1,-.333333))
# roots.append(bisection(-.333333,.333333))
# roots.append(bisection(.333333,1))

# print(roots)
