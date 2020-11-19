from function import f

def fiveEnd(x,h):
    return 1/(12*h)*(-25*f(x) + 48*f(x+h) - 36*f(x +2*h)+ 16*f(x+3*h) -3*f(x+4*h))