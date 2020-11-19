from f import f
n = 2
def simp(a,b):
    h = (b-a)/n
    mid = a+h
    return (h/3)*(f(a) + 4*f(mid) + f(b))

print(simp(3,4))

