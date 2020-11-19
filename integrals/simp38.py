from f import f
n = 3
def simp(a,b):
    h = (b-a)/n
    midL = (2*a+b)/3
    midR = (a+2*b)/3
    return (3*h/8)*(f(a) + 3*f(midL) + 3*f(midR) + f(b))

print(simp(3,4))
