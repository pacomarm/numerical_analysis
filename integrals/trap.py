from f import f

n = 1

def trap(a,b):
    h = (b-a)/n
    return h/2*(f(a)+f(b))