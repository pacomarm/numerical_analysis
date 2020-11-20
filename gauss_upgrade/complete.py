from f       import f
from roots   import bisection
from simpson import simpson

n = 5
roots = []
coef  = []

def getRoots(n):
    h = 2/n
    a = -1
    b = a + h
    while(len(roots) < n):
        roots.append(bisection(a,b))
        a = b
        b = a + h

def getCoeff(n):
    for i in range(n):
        coef.append(simpson(i,-1,0,1, roots,n))

def getGauss(n):
    getRoots(n)
    getCoeff(n)
    suma = 0
    for i in range(n):
        suma += (coef[i]*f(roots[i]))
    return suma

print(getGauss(5))
    

