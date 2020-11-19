from function import f

def threeEnd(x,h):
    return 1/(2*h)*(-3*f(x) + 4*f(x+h) - f(x +2*h))
