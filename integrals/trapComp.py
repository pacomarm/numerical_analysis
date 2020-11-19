from f import f


def trapComp(a,b,m):
    suma = .5*f(a) + .5*f(b)
    h = (b-a)/m
    z = a + h
    while(z < b):
        suma+=f(z)
        z+=h
    return h*suma

print(trapComp(0,10,200))

